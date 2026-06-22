import threading

from corelib.network import DroneClient
from src.network.transports.base import BaseTransport


class WiFiTransport(BaseTransport):

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 7000
    ):

        self.client = DroneClient(
            host,
            port
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

    def disconnect(self):

        self.connected = False

        self.client.close()

    def send(self, message):

        self.client.send(message)

    def receive(self):

        return self.client.receive()

    def is_connected(self):

        return self.connected

    def subscribe(self, callback):

        self.callbacks.append(callback)

    def receive_loop(self):

        while self.connected:

            try:

                message = self.client.receive()

                print(f"[WiFi] RX -> {message.type}")

                for callback in self.callbacks:

                    callback(message)

            except Exception as e:

                print(e)

                self.connected = False