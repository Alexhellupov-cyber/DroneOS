import serial


class SerialDriver:

    def __init__(self, port: str, baudrate: int = 115200):

        self.port = port
        self.baudrate = baudrate

        self.serial = None

    def connect(self):

        self.serial = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=0,
            write_timeout=0
        )

    def disconnect(self):

        if self.serial:

            self.serial.close()

    def send(self, data: bytes):

        self.serial.flush()



    def receive(self, size: int) -> bytes:

        return self.serial.read(size)