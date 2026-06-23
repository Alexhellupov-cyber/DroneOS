from src.input.usb_input import USBInput


class RCService:

    def __init__(self):

        self.input = USBInput()

    def update(self):

        return self.input.update()