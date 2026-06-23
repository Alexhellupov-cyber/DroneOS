from src.drivers.crsf.encoder import CRSFPacker


class CRSFDriver:

    def __init__(self, serial_driver):

        self.serial = serial_driver

    def send(self, packet):

        channels = [

            CRSFPacker.rc_to_crsf(packet.roll),
            CRSFPacker.rc_to_crsf(packet.pitch),
            CRSFPacker.rc_to_crsf(packet.yaw),
            CRSFPacker.rc_to_crsf(packet.throttle),

            CRSFPacker.rc_to_crsf(packet.aux1),
            CRSFPacker.rc_to_crsf(packet.aux2),
            CRSFPacker.rc_to_crsf(packet.aux3),
            CRSFPacker.rc_to_crsf(packet.aux4),

            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
            CRSFPacker.rc_to_crsf(1000),
        ]

        frame = CRSFPacker.encode(channels)

        self.serial.send(frame)