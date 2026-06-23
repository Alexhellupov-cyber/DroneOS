class ChannelMapper:

    @staticmethod
    def axis_to_rc(value: float) -> int:
        """
        pygame:
            -1.0 ... +1.0

        RC:
            1000 ... 2000
        """

        value = max(-1.0, min(1.0, value))

        return int(((value + 1.0) / 2.0) * 1000 + 1000)