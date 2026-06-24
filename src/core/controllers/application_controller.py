from src.network.network_manager import NetworkManager
from src.core.services.rc_service import RCService
from src.core.services.network_service import NetworkService


class ApplicationController:

    def __init__(self, network):

        self.network = network

        self.network_service = NetworkService(
            self.network
        )

        self.rc = RCService()

    def connect_ground(self):

        self.network.connect()

    def update(self):

        packet = self.rc.update()

        print("RC:", packet)

        self.network_service.send_rc(
            packet
        )

        return packet