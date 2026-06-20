import socket
import struct
import json


class DroneOSClient:

    def __init__(self, host="127.0.0.1", port=7000):

        self.host = host
        self.port = port

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

    def connect(self):

        self.socket.connect(
            (
                self.host,
                self.port
            )
        )

    def _recv_exact(self, size):

        data = b""

        while len(data) < size:

            packet = self.socket.recv(
                size - len(data)
            )

            if not packet:
                return None

            data += packet

        return data

    def receive(self):

        header = self._recv_exact(4)

        if header is None:
            return None

        length = struct.unpack(">I", header)[0]

        payload = self._recv_exact(length)

        if payload is None:
            return None

        return json.loads(
            payload.decode()
        )