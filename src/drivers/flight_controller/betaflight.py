from src.drivers.serial_driver import SerialDriver
from src.drivers.flight_controller.base import FlightController


class BetaflightDriver(FlightController):

    def __init__(self):

        self.serial = SerialDriver(
            "/dev/serial0",
            115200
        )

    def connect(self):

        self.serial.connect()