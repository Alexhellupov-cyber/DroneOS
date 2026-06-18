import socket

from common.config import HOST, PORT


class DroneServer:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()

        print(f"[NETWORK] Listening on {HOST}:{PORT}")

    def accept(self):
        return self.server.accept()
