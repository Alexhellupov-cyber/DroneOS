from dataclasses import dataclass


@dataclass
class CRSFPacket:

    roll: int = 1500
    pitch: int = 1500
    yaw: int = 1500
    throttle: int = 1000

    aux1: int = 1000
    aux2: int = 1000
    aux3: int = 1000
    aux4: int = 1000