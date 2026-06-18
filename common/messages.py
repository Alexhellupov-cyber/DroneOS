from enum import Enum


class MessageType(Enum):

    PING = "ping"

    PONG = "pong"

    TELEMETRY = "telemetry"

    COMMAND = "command"

    HEARTBEAT = "heartbeat"

    VIDEO = "video"

    ERROR = "error"
