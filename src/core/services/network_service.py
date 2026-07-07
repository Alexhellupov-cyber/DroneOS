from importlib.metadata.diagnose import inspect

from corelib.messages import rc


class NetworkService:

    def __init__(self, network):

        self.network = network

    def send_rc(self, packet):

        self.network.send(
            rc(
                packet.to_dict()
            )
        )