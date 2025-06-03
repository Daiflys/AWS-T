import json
import psycopg2
import boto3


def get_db_credentials(secret_name):
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])
    return secret

def handler(event, context):
    # Obtener el término de búsqueda del query string
    search_term = event.get("queryStringParameters", {}).get("q", "Ancestral")
    if not search_term:
        search_term = "Ancestral"

    try:
        creds = get_db_credentials("mtg-db-credentials")
        print(" Obtuve secretos:", creds)
        conn = psycopg2.connect(
            host=creds["host"],
            database=creds["dbInstanceIdentifier"],
            user=creds["username"],
            password=creds["password"],
            port=creds.get("port", 5432),
            connect_timeout=5 #seconds
        )
        cur = conn.cursor()

        # Búsqueda por nombre parcial (ignorando mayúsculas/minúsculas)
        query = """
            SELECT scryfall_id, set_name, card_type, mana_cost, name_en, image_url
            FROM cards
            WHERE LOWER(name_en) LIKE %s
            LIMIT 20
        """
        cur.execute(query, (f"%{search_term.lower()}%",))
        rows = cur.fetchall()

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