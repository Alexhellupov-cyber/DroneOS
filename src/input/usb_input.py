import pygame
from src.input.channel_mapper import ChannelMapper
from src.input.rc_packet import RCPacket
from src.input.channel_mapper import ChannelMapper


class USBInput:

    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise Exception("Joystick not found")

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        print(f"Connected: {self.joystick.get_name()}")

    def update(self):

        pygame.event.pump()

        packet = RCPacket()

        packet.roll = ChannelMapper.axis_to_rc(
            self.joystick.get_axis(0)
        )

        packet.pitch = ChannelMapper.axis_to_rc(
            self.joystick.get_axis(1)
        )

        packet.yaw = ChannelMapper.axis_to_rc(
            self.joystick.get_axis(2)
        )

        packet.throttle = ChannelMapper.throttle_to_rc(
            self.joystick.get_axis(3)
        )

        return packet