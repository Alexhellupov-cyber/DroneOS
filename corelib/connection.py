import socket
import struct

from corelib.protocol import encode, decode
from corelib.logger import get_logger

logger = get_logger()


class Connection:

    def __init__(self, sock: socket.socket):
        self.socket = sock

    def _recv_exact(self, size: int):

        data = b""

        while len(data) < size:

            chunk = self.socket.recv(size - len(data))

            if not chunk:
                return None

            data += chunk

        return data

    def receive(self):

        header = self._recv_exact(4)

        if header is None:
            return None

        length = struct.unpack(">I", header)[0]

        payload = self._recv_exact(length)

        if payload is None:
            return None

        message = decode(payload)

        logger.info(f"RX -> {message}")

        return message

    def send(self, message):

        payload = encode(message)

        header = struct.pack(">I", len(payload))

        self.socket.sendall(header + payload)

        logger.info(f"TX -> {message}")

    def close(self):
        self.socket.close()