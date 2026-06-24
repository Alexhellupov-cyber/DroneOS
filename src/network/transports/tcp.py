import threading

from corelib.network import DroneClient
from src.network.transports.base import BaseTransport


class TCPTransport(BaseTransport):

    def __init__(self,
                 host="192.168.0.143",
                 port=7000):

        self.host = host
        self.port = port

        self.client = DroneClient(
            host,
            port
        )

        self.connected = False

        self.callbacks = []

    def connect(self):

        print("TCPTransport client:", id(self.client))
        print("Socket before connect:", self.client.socket.fileno())

        self.client.connect()

        print("Socket after connect:", self.client.socket.fileno())

        self.connected = True

        threading.Thread(
            target=self.receive_loop,
            daemon=True
        ).start()

        return True

    def disconnect(self):

        self.connected = False

    def send(self, message):

        print("SEND client:", id(self.client))
        print("SEND socket:", self.client.socket.fileno())

        self.client.send(message)
    
    def receive(self):

        return self.client.receive()


    def is_connected(self) -> bool:

        return self.connected

    def subscribe(self, callback):

        self.callbacks.append(callback)

    def receive_loop(self):

        while self.connected:

            try:

                message = self.client.receive()

                for callback in self.callbacks:

                    callback(message)

            except Exception as e:

                print(e)

                self.connected = False
                break