from src.network.manager import ConnectionManager
from src.network.transports.wifi import WiFiTransport


class NetworkManager:

    def __init__(self):

        self.connection = ConnectionManager()

        self.connection.add_transport(
            WiFiTransport()
        )

    def connect(self):

        return self.connection.connect()

    def send(self, message):

        self.connection.send(message)

    def receive(self):

        return self.connection.receive()
    
    def subscribe(self, callback):

        self.connection.active_transport.subscribe(
            callback
        )