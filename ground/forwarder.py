from ground.logger import logger


class Forwarder:

    def __init__(self, bridge):
        self.bridge = bridge

    def forward(self, message):

        logger.info(
            f"Forwarding {message.type}"
        )

        self.bridge.broadcast(message)