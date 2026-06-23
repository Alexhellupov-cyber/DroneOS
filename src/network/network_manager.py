from src.network.transport_manager import ConnectionManager
from src.network.transports.tcp import TCPTransport
from src.network.transports.serial import SerialTransport
from src.config.config_manager import ConfigManager


class NetworkManager:

    def __init__(self):
        self.config = ConfigManager()
        self.connection = ConnectionManager()

        # Регистрируем транспорт
        self.connection.register_transport(
            "tcp",
            TCPTransport(

                host=self.config.get(
                    "tcp",
                    "host"
                ),

                port=self.config.get(
                    "tcp",
                    "port"
                )

            )
        )

        # Регистрируем сериальный транспорт
        self.connection.register_transport(
            "serial",
            SerialTransport(

                port=self.config.get(
                    "serial",
                    "port"
                ),

                baudrate=self.config.get(
                    "serial",
                    "baudrate"
                )

            )
        )

        # Делаем его активным
        self.connection.set_active_transport(
            "tcp"
        )

    def connect(self, transport="tcp"):

        return self.connection.connect(
            transport
        )

    def disconnect(self):

        return self.connection.disconnect()

    def send(self, message):

        self.connection.send(message)

    def receive(self):

        return self.connection.receive()

    def subscribe(self, callback):

        self.connection.subscribe(callback)