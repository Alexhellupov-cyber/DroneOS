import socket
import time


class DroneServer:

    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((host, port))
        self.server.listen(1)

        print(f"[NETWORK] Listening on {host}:{port}")

    def wait_connection(self):
        print("[NETWORK] Waiting for client...")

        conn, addr = self.server.accept()

        print(f"[NETWORK] Client connected: {addr}")

        return conn, addr


class DroneClient:

    def __init__(self, host, port=5000):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):

        while True:

            try:

                print("[NETWORK] Connecting...")

                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                self.socket.connect((self.host, self.port))

                print("[NETWORK] Connected")

                return

            except Exception:

                print("[NETWORK] Retry in 2 sec...")

                time.sleep(2)

    def send(self, data):
        self.socket.sendall(data)

    def receive(self):
        return self.socket.recv(4096)
