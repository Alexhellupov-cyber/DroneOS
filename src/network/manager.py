from src.network.transports.base import BaseTransport


class ConnectionManager:

    def __init__(self):

        self.transports = []

        self.active_transport = None

    def add_transport(self, transport: BaseTransport):

        self.transports.append(transport)

    def connect(self):

        for transport in self.transports:

            try:

                transport.connect()

                self.active_transport = transport

                print(f"Connected using {transport.__class__.__name__}")

                return True

            except Exception as e:

                print(e)

        return False

    def disconnect(self):

        if self.active_transport:

            self.active_transport.disconnect()

    def send(self, message):

        if self.active_transport:

            self.active_transport.send(message)

    def receive(self):

        if self.active_transport:

            return self.active_transport.receive()