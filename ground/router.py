from ground.logger import logger


class Router:

    def __init__(self, bridge):
        self.bridge = bridge

    def route(self, message):

        logger.info(
            f"Route: {message.type}"
        )

        if message.target == "desktop":

            self.bridge.broadcast(message)

        elif message.target == "ground":

            logger.info(
                "Message for Ground"
            )

        elif message.target == "onboard":

            logger.info(
                "Message for Onboard"
            )

        else:

            logger.warning(
                f"Unknown target: {message.target}"
            )