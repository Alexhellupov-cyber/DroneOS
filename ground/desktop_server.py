import socket

from corelib.config import DESKTOP_BIND_HOST, DESKTOP_PORT
from corelib.connection import Connection
from corelib.logger import get_logger

logger = get_logger()


class DesktopServer:

    def __init__(self, bridge):

        self.bridge = bridge

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
                DESKTOP_BIND_HOST,
                DESKTOP_PORT
            )
        )

        self.server.listen()

        logger.info(
            f"Desktop server on {DESKTOP_PORT}"
        )

    def start(self):

        while True:

            sock, address = self.server.accept()

            logger.info(
                f"Desktop connected: {address}"
            )

            connection = Connection(sock)

            self.bridge.add(connection)