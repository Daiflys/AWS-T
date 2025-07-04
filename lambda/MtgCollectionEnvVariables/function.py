import json
import psycopg2

def handler(event, context):
    # Obtener el término de búsqueda del query string
    print("handler start")
    search_term = event.get("queryStringParameters", {}).get("q", "Ancestral")
    if not search_term:
        search_term = "Ancestral"

    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            port=int(os.environ.get("DB_PORT", 5432)),
            connect_timeout=5 #seconds
        )
        cur = conn.cursor()

        # Búsqueda por nombre parcial (ignorando mayúsculas/minúsculas)
        query = """
            SELECT scryfall_id, set_name, card_type, mana_cost, name_enA, image_url
            FROM cards
            WHERE LOWER(name_en) LIKE %s
            LIMIT 20
        """
        print("going to execute query")
        cur.execute(query, (f"%{search_term.lower()}%",))
        rows = cur.fetchall()
        print("query executed")
        results = []
        for row in rows:
            results.append({
                "scryfall_id": row[0],
                "set_name": row[1],
                "card_type": row[2],
                "mana_cost": row[3],
                "name_en": row[4],
                "image_url" : row[5],
            })

        cur.close()
        conn.close()

        return {
            "statusCode": 200,
            "body": json.dumps(results)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }