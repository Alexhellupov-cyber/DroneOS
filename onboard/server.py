import socket
import json

from src.drivers.crsf.driver import CRSFDriver
from src.input.rc_packet import RCPacket

HOST = "0.0.0.0"
PORT = 5000


class OnboardServer:

    def __init__(self):

        self.crsf = CRSFDriver()

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server.bind((HOST, PORT))
        self.server.listen(1)

        print(f"Listening {HOST}:{PORT}")

    def start(self):

        while True:

            client, addr = self.server.accept()

            print(addr)

            while True:

                data = client.recv(4096)

                if not data:
                    break

                try:

                    message = json.loads(
                        data.decode()
                    )

                    if message["type"] != "rc":
                        continue

                    packet = RCPacket(
                        **message["payload"]
                    )

                    self.crsf.send(packet)

                except Exception as e:

                    print(e)

            client.close()

    if __name__ == "__main__":
        server = OnboardServer()
        server.start()