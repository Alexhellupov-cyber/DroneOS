from src.drivers.crsf.crc import CRSFCRC


class CRSFPacker:

    ADDRESS = 0xC8
    TYPE = 0x16

    @staticmethod
    def encode(channels):

        if len(channels) != 16:
            raise ValueError("CRSF requires 16 channels")

        payload = bytearray()

        bits = 0
        bit_count = 0

        for ch in channels:

            ch &= 0x07FF

            bits |= ch << bit_count
            bit_count += 11

            while bit_count >= 8:
                payload.append(bits & 0xFF)
                bits >>= 8
                bit_count -= 8

        if bit_count:
            payload.append(bits & 0xFF)

        frame = bytearray()

        frame.append(0xC8)
        frame.append(24)
        frame.append(0x16)

        frame.extend(payload[:22])

        crc = CRSFCRC.calculate(frame[2:])

        frame.append(crc)

        return bytes(frame)