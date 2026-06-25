from src.drivers.crsf.crc import CRSFCRC


class CRSFPacker:

    ADDRESS = 0xC8
    TYPE = 0x16

    @staticmethod
    def rc_to_crsf(value: int):

        value = max(1000, min(2000, value))

    @staticmethod
    def rc_to_crsf(value: int):

        value = max(1000, min(2000, value))

        return round(
            172 + (value - 1000) * (1811 - 172) / 1000
        )

    @staticmethod
    def encode(channels):

        packed = 0
        bits = 0

        payload = bytearray()

        for ch in channels:

            packed |= (ch & 0x7FF) << bits

            bits += 11

            while bits >= 8:

                payload.append(
                    packed & 0xFF
                )

                packed >>= 8

                bits -= 8

        if bits:

            payload.append(
                packed & 0xFF
            )

        frame = bytearray()

        frame.append(
            CRSFPacker.ADDRESS
        )

        frame.append(
            len(payload) + 2
        )

        frame.append(
            CRSFPacker.TYPE
        )

        frame.extend(payload)

        crc = CRSFCRC.calculate(
            frame[2:]
        )

        frame.append(crc)

        return bytes(frame)