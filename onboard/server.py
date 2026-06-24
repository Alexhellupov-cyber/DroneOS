import socket
import json
from corelib.network import DroneServer
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

        self.server = DroneServer(
            HOST,
            PORT
        )

    def start(self):

        while True:

            connection, addr = self.server.accept()

            print(addr)

            while True:

                try:

                    message = connection.receive()

                    if message is None:
                        break

                    if message["type"] != "rc":
                        continue

                    packet = RCPacket(
                        **message["payload"]
                    )
                    print(packet)
                    self.crsf.send(packet)

                except Exception as e:

                    print(e)

            connection.close()

if __name__ == "__main__":
        server = OnboardServer()
        server.start()