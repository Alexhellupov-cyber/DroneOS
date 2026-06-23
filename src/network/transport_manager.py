from src.network.transports.base import BaseTransport


class ConnectionManager:

    def __init__(self):

        self.transports = {}

        self.active_transport = None

    def register_transport(self, name, transport):

        self.transports[name] = transport

    def get_transport(self, name):

        return self.transports.get(name)
    
    def set_active_transport(self, name):

        transport = self.get_transport(name)

        if transport is None:

            raise Exception(
                f"Transport '{name}' not found."
            )

        self.active_transport = transport

    def connect(self, transport_name=None):

        if transport_name == "auto":

            print("Searching transport...")

            for name, transport in self.transports.items():

                try:

                    print(f"Trying {name}...")

                    transport.connect()

                    self.active_transport = transport

                    print(f"Connected via {name}")

                    return

                except Exception as e:

                    print(e)

            raise Exception(
                "No available transport."
            )

        if transport_name is not None:

            self.set_active_transport(
                transport_name
            )

        if self.active_transport is None:

            raise Exception(
                "No active transport selected."
            )

        self.active_transport.connect()

    def disconnect(self):

        if self.active_transport:

            self.active_transport.disconnect()

    def send(self, message):

        if self.active_transport:

            self.active_transport.send(message)

    def receive(self):

        if self.active_transport:

            return self.active_transport.receive()
        
    def subscribe(self, callback):

        if self.active_transport:

            self.active_transport.subscribe(callback)

    def available_transports(self):

        return list(
            self.transports.keys()
        )