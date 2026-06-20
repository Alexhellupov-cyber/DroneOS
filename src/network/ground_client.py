import threading

from corelib.network import DroneClient


class GroundClient:

    def __init__(self):

        self.client = DroneClient(
            "192.168.0.143",
            7000
        )

        self.connected = False

        self.callbacks = []

    def connect(self):

        self.client.connect()

        self.connected = True

        threading.Thread(
            target=self.receive_loop,
            daemon=True
        ).start()

    def subscribe(self, callback):

        self.callbacks.append(callback)

    def receive_loop(self):

        while self.connected:

            try:

                message = self.client.receive()

                print("RX:", message)

                for callback in self.callbacks:

                    callback(message)

            except Exception as e:

                print(e)

                self.connected = False