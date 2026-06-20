import socket

from corelib.connection import Connection
from corelib.logger import get_logger

logger = get_logger()


class DroneServer:

    def __init__(self, host: str, port: int):

        self.host = host
        self.port = port

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        self.server.bind(
            (
                self.host,
                self.port
            )
        )

        self.server.listen()

        logger.info(
            f"Listening on {self.host}:{self.port}"
        )

    def accept(self):

        logger.info("Waiting for client...")

        client_socket, address = self.server.accept()

        logger.info(
            f"Client connected: {address}"
        )

        return Connection(client_socket), address

    def close(self):

        self.server.close()


class DroneClient:

    def __init__(self, host: str, port: int):

        self.host = host
        self.port = port

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.connection = Connection(
            self.socket
        )

    def connect(self):

        logger.info(
            f"Connecting to {self.host}:{self.port}"
        )

        self.socket.connect(
            (
                self.host,
                self.port
            )
        )

        logger.info("Connected")

    def send(self, message):

        self.connection.send(message)

    def receive(self):

        return self.connection.receive()

    def close(self):

        logger.info("Disconnected")

        self.connection.close()