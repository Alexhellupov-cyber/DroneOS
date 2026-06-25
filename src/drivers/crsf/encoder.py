from src.drivers.crsf.crc import CRSFCRC


class CRSFPacker:

    ADDRESS = 0xC8
    TYPE = 0x16

    @staticmethod
    def rc_to_crsf(value: int) -> int:
        """
        Преобразование RC 1000..2000 -> CRSF 172..1811
        """
        value = max(1000, min(2000, value))

        return round(
            172 + (value - 1000) * (1811 - 172) / 1000
        )

    @staticmethod
    def encode(channels):

        if len(channels) != 16:
            raise ValueError(
                "CRSF requires exactly 16 channels"
            )

        payload = bytearray(22)

        bit_index = 0

        for ch in channels:

            ch &= 0x07FF

            byte_index = bit_index // 8
            shift = bit_index % 8

            value = ch << shift

            payload[byte_index] |= value & 0xFF

            if byte_index + 1 < len(payload):
                payload[byte_index + 1] |= (value >> 8) & 0xFF

            if byte_index + 2 < len(payload):
                payload[byte_index + 2] |= (value >> 16) & 0xFF

            bit_index += 11

        frame = bytearray()

        frame.append(CRSFPacker.ADDRESS)
        frame.append(24)
        frame.append(CRSFPacker.TYPE)

        frame.extend(payload)

        crc = CRSFCRC.calculate(
            frame[2:]
        )

        frame.append(crc)

        return bytes(frame)