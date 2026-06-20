import json

from corelib.message import Message


def encode(message: Message) -> bytes:
    return json.dumps(
        message.to_dict()
    ).encode()


def decode(data: bytes) -> Message:
    packet = json.loads(data.decode())
    return Message.from_dict(packet)