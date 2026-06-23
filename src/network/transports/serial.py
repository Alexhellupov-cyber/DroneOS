from src.network.transports.base import BaseTransport


class SerialTransport(BaseTransport):

    def __init__(self,
                 port="/dev/serial0",
                 baudrate=115200):

        self.port = port
        self.baudrate = baudrate

        self.serial = None

    def connect(self):

        raise NotImplementedError(
            "Serial transport is not implemented yet."
        )

    def disconnect(self):

        if self.serial:

            self.serial.close()

    def send(self, message):

        raise NotImplementedError()

    def receive(self):

        raise NotImplementedError()

    def is_connected(self):

        return self.serial is not None