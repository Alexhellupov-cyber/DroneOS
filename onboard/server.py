import threading
import time

from corelib.network import DroneServer
from src.drivers.crsf.driver import CRSFDriver
from src.input.rc_packet import RCPacket

HOST = "0.0.0.0"
PORT = 5001


class OnboardServer:

    def __init__(self):

        self.crsf = CRSFDriver()

        self.server = DroneServer(
            HOST,
            PORT
        )

        self.last_packet = RCPacket(
            roll=1500,
            pitch=1500,
            throttle=1000,
            yaw=1500,
            aux1=1000,
            aux2=1000,
            aux3=1000,
            aux4=1000
        )
        print(self.last_packet)
    def crsf_loop(self):

        while True:
            self.crsf.send(self.last_packet)
            time.sleep(0.004)   # 250 Гц

    def start(self):

        threading.Thread(
            target=self.crsf_loop,
            daemon=True
        ).start()

        while True:

            connection, addr = self.server.accept()

            print("Ground connected:", addr)

            while True:

                try:

                    message = connection.receive()

                    if message is None:
                        break

                    if message.id != "rc":
                        continue

                    self.last_packet = RCPacket(
                        **message.payload
                    )

                    print("RECEIVED:", self.last_packet)
                except Exception as e:

                    print(e)
                    break

            connection.close()


if __name__ == "__main__":
    OnboardServer().start()