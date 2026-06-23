from src.network.network_manager import NetworkManager


class ApplicationController:

    def __init__(self):

        self.network = NetworkManager()

    def connect_ground(self):

        self.network.connect()