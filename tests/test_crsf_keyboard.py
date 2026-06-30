import time
import keyboard

from src.drivers.crsf.driver import CRSFDriver
from src.input.rc_packet import RCPacket

driver = CRSFDriver()

packet = RCPacket()

packet.roll = 1500
packet.pitch = 1500
packet.yaw = 1500
packet.throttle = 1000

packet.aux1 = 1000

print("1 = ARM")
print("2 = DISARM")
print("W/S = THROTTLE")
print("A/D = YAW")
print("←/→ = ROLL")
print("↑/↓ = PITCH")

while True:

    if keyboard.is_pressed("1"):
        packet.aux1 = 2000

    if keyboard.is_pressed("2"):
        packet.aux1 = 1000

    if keyboard.is_pressed("w"):
        packet.throttle = min(2000, packet.throttle + 5)

    if keyboard.is_pressed("s"):
        packet.throttle = max(1000, packet.throttle - 5)

    if keyboard.is_pressed("a"):
        packet.yaw = max(1000, packet.yaw - 5)

    if keyboard.is_pressed("d"):
        packet.yaw = min(2000, packet.yaw + 5)

    if keyboard.is_pressed("left"):
        packet.roll = max(1000, packet.roll - 5)

    if keyboard.is_pressed("right"):
        packet.roll = min(2000, packet.roll + 5)

    if keyboard.is_pressed("up"):
        packet.pitch = min(2000, packet.pitch + 5)

    if keyboard.is_pressed("down"):
        packet.pitch = max(1000, packet.pitch - 5)

    driver.send(packet)

    print(
        f"\rARM={packet.aux1} "
        f"T={packet.throttle} "
        f"R={packet.roll} "
        f"P={packet.pitch} "
        f"Y={packet.yaw}",
        end=""
    )

    time.sleep(0.004)