from .commands import MSP as Commands


class MSP:

    HEADER_REQUEST = b"$M<"
    HEADER_RESPONSE = b"$M>"

    def __init__(self, serial):

        self.serial = serial

    def request(self, command, payload=b""):

        size = len(payload)

        checksum = size ^ command

        for byte in payload:
            checksum ^= byte

        packet = (
            self.HEADER_REQUEST +
            bytes([size]) +
            bytes([command]) +
            payload +
            bytes([checksum])
        )

        self.serial.send(packet)

        return self.read_packet()
    
    def read_packet(self):

        header = self.serial.receive(3)

        if header != self.HEADER_RESPONSE:
            raise Exception(
                f"Invalid MSP header: {header}"
            )

        size = self.serial.receive(1)[0]

        command = self.serial.receive(1)[0]

        payload = self.serial.receive(size)

        checksum = self.serial.receive(1)[0]

        calculated = size ^ command

        for byte in payload:
            calculated ^= byte

        if calculated != checksum:
            raise Exception(
                "MSP checksum error"
            )

        return {
            "command": command,
            "payload": payload,
            "checksum": checksum
        }