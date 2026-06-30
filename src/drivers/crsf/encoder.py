from src.drivers.crsf.crc import CRSFCRC


class CRSFCRC:

    POLY = 0xD5

    @staticmethod
    def calculate(data):

        crc = 0

        for byte in data:

            crc ^= byte

            for _ in range(8):

                if crc & 0x80:
                    crc = ((crc << 1) ^ CRSFCRC.POLY) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF

        return crc


class CRSFPacker:

    @staticmethod
    def rc_to_crsf(value: int) -> int:
        """
        RC 1000..2000 -> CRSF 172..1811
        """
        value = max(1000, min(2000, value))
        return int((value - 1000) * (1811 - 172) / 1000 + 172)

    @staticmethod
    def encode(channels):

        if len(channels) != 16:
            raise ValueError("CRSF requires exactly 16 channels")

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

        frame.append(0xC8)      # Device address
        frame.append(24)        # Length
        frame.append(0x16)      # RC Channels Packed

        frame.extend(payload[:22])

        crc = CRSFCRC.calculate(frame[2:])

        frame.append(crc)

        return bytes(frame)