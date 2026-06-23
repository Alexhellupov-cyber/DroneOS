class CRSFCRC:

    POLY = 0xD5

    @staticmethod
    def calculate(data: bytes) -> int:

        crc = 0

        for byte in data:

            crc ^= byte

            for _ in range(8):

                if crc & 0x80:
                    crc = ((crc << 1) ^ CRSFCRC.POLY) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF

        return crc