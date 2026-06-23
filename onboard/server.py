import socket
import json

HOST = "0.0.0.0"
PORT = 5000


class OnboardServer:

    def __init__(self):

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server.bind((HOST, PORT))
        self.server.listen(1)

        print(f"Listening on {HOST}:{PORT}")

    def start(self):

        while True:

            client, address = self.server.accept()

            print(f"Ground connected: {address}")

            while True:

                data = client.recv(4096)

                if not data:
                    break

                try:

                    message = json.loads(
                        data.decode()
                    )

                    print(message)

                except Exception as e:

                    print(e)

            client.close()