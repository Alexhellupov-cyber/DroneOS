from corelib.message import Message


def ping():
    return Message(
        type="ping",
        source="ground",
        target="onboard"
    )


def pong():
    return Message(
        type="pong",
        source="onboard",
        target="ground"
    )


def telemetry(payload):
    return Message(
        type="telemetry",
        source="onboard",
        target="desktop",
        payload=payload
    )


def heartbeat():
    return Message(
        type="heartbeat",
        source="onboard",
        target="ground"
    )

def rc(payload):
    return Message(
        type="rc",
        source="ground",
        target="onboard",
        payload=payload
    )