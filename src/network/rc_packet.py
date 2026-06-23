from dataclasses import dataclass


@dataclass
class RCPacket:

    roll: int = 1500
    pitch: int = 1500
    yaw: int = 1500
    throttle: int = 1000

    aux1: int = 1000
    aux2: int = 1000
    aux3: int = 1000
    aux4: int = 1000

    def to_dict(self):

        return {
            "roll": self.roll,
            "pitch": self.pitch,
            "yaw": self.yaw,
            "throttle": self.throttle,
            "aux1": self.aux1,
            "aux2": self.aux2,
            "aux3": self.aux3,
            "aux4": self.aux4,
        }