from src.input.rc_packet import RCPacket


class InputManager:

    def __init__(self):

        self.packet = RCPacket()

    def get_packet(self):

        return self.packet