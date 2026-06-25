from src.input.usb_input import USBInput


class RCService:

    def __init__(self):

        self.input = USBInput()

        self.armed = False

    def set_arm(self, value: bool):

        self.armed = value

    def update(self):

        packet = self.input.update()

        packet.aux1 = 2000 if self.armed else 1000

        return packet