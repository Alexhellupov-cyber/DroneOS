from src.drivers.serial_driver import SerialDriver
from src.drivers.crsf.encoder import CRSFPacker
from src.input.rc_packet import RCPacket


class CRSFDriver:

    def __init__(self):

        self.serial = SerialDriver(
            "/dev/serial0",
            420000
        )

        self.serial.connect()

    def send(self, packet: RCPacket):

        channels = [

            packet.roll,
            packet.pitch,
            packet.throttle,
            packet.yaw,

            packet.aux1,
            packet.aux2,
            packet.aux3,
            packet.aux4,

            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000

        ]

        channels = [
            CRSFPacker.rc_to_crsf(x)
            for x in channels
        ]

        frame = CRSFPacker.encode(
            channels
        )

        print("CHANNELS:", channels)
        print("FRAME:", frame.hex())
        self.serial.send(frame)

        print(channels)

        frame = Encoder.encode(channels)
        print(frame.hex())
        self.serial.send(frame)