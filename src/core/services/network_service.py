from importlib.metadata.diagnose import inspect

from corelib.messages import rc


class NetworkService:

    def __init__(self, network):

        self.network = network

    def send_rc(self, packet):

        print("SEND RC")
        print("TYPE:", type(packet))
        print("FILE:", inspect.getfile(packet.__class__))
        print("HAS to_dict:", hasattr(packet, "to_dict"))
        print("DICT:", packet.__dict__)

        self.network.send(
            rc(
                packet.to_dict()
            )
        )