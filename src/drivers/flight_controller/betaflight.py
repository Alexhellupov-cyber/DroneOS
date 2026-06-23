from src.drivers.serial_driver import SerialDriver
from src.drivers.flight_controller.base import FlightController
from src.drivers.flight_controller.protocol.msp import MSP
from src.drivers.flight_controller.protocol.commands import MSP as Commands


class BetaflightDriver(FlightController):

    def __init__(self):

        self.serial = SerialDriver(
            "/dev/serial0",
            115200
        )

        self.msp = MSP(self.serial)

    def connect(self):
        self.serial.connect()

    def disconnect(self):
        self.serial.disconnect()

    def get_api_version(self):
        return self.msp.request(
            Commands.API_VERSION
        )

    def arm(self):
        print("ARM")

    def disarm(self):
        print("DISARM")

    def send_rc(
        self,
        roll,
        pitch,
        yaw,
        throttle,
        aux1=1000,
        aux2=1000,
        aux3=1000,
        aux4=1000,
    ):
        print(f"RC: {roll} {pitch} {yaw} {throttle}")

    def get_telemetry(self):
        return {}

    def test(self):

        self.connect()

        response = self.get_api_version()

        print(response)

        self.disconnect()