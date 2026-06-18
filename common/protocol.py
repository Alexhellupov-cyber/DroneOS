import json


def encode(message_type, payload=None):

    if payload is None:
        payload = {}

    packet = {
        "type": message_type,
        "payload": payload
    }

    return (json.dumps(packet) + "\n").encode()


def decode(data):

    return json.loads(data.decode())
