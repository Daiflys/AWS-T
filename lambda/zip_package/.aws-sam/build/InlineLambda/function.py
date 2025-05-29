import json

def handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])

    # a Python object (dict):
    info = {
        "Type": "Zip Package",
        "Version": 1
    }

    # convert into JSON:
    info_json = json.dumps(info)

    # the result is a JSON string:
    print(info_json)

    return {
        'message' : message
    }
