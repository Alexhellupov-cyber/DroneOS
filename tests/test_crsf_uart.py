import time

from src.drivers.serial_driver import SerialDriver
from src.drivers.crsf.encoder import CRSFPacker


serial = SerialDriver(
    "/dev/serial0",
    420000
)

serial.connect()

channels = [
    CRSFPacker.rc_to_crsf(1500),
    CRSFPacker.rc_to_crsf(1500),
    CRSFPacker.rc_to_crsf(1000),
    CRSFPacker.rc_to_crsf(1000),
    CRSFPacker.rc_to_crsf(1000),
    CRSFPacker.rc_to_crsf(1000),
    CRSFPacker.rc_to_crsf(1000),
    CRSFPacker.rc_to_crsf(1000),
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

print(frame.hex())

while True:

    serial.send(frame)

    time.sleep(0.01)