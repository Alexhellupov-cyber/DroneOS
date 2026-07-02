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

    @staticmethod
    def throttle_to_rc(value: float) -> int:
        """
        Инвертированный газ.
        Вверх = 2000
        Вниз = 1000
        """

        value = max(-1.0, min(1.0, value))

        value = -value

        return int(((value + 1.0) / 2.0) * 1000 + 1000)