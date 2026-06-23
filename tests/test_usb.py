from src.input.usb_input import USBInput

usb = USBInput()

while True:

    packet = usb.update()

    print(packet.to_dict())