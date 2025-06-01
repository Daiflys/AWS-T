import json
from faker import Faker

def handler(event, context):
    fake = Faker()

    message = 'Hello {} {}!'.format(fake.name())

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
