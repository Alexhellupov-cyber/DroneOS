import time

from src.drivers.crsf.driver import CRSFDriver
from src.input.rc_packet import RCPacket

driver = CRSFDriver()

packet = RCPacket()
packet.roll = 1500
packet.pitch = 1500
packet.yaw = 1500
packet.throttle = 1000
packet.aux1 = 1000

print("Starting automatic CRSF test...")

start = time.time()

while True:
    t = time.time() - start

    if t < 2:
        packet.aux1 = 1000
        packet.throttle = 1000
        print("Waiting...", end="\r")

    elif t < 4:
        packet.aux1 = 2000
        packet.throttle = 1000
        print("ARM", end="\r")

    elif t < 6:
        packet.throttle = 1100
        print("Throttle 1100", end="\r")

    elif t < 8:
        packet.throttle = 1200
        print("Throttle 1200", end="\r")

    elif t < 10:
        packet.throttle = 1000
        print("Throttle 1000", end="\r")

    else:
        packet.aux1 = 1000
        packet.throttle = 1000
        print("\nDISARM")
        break

    driver.send(packet)
    time.sleep(0.004)

print("Done.")