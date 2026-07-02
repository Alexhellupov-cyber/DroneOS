import time
from ground.rc_sender import RCSender
from corelib.config import ONBOARD_CONNECT_HOST, ONBOARD_PORT
from corelib.logger import get_logger
from corelib.network import DroneClient

logger = get_logger()


class GroundDroneClient:

    def __init__(self, router):

        self.router = router

    def start(self):

        while True:

            client = DroneClient(
                ONBOARD_CONNECT_HOST,
                ONBOARD_PORT
            )

            try:

                client.connect()                
                logger.info("Connected to onboard")
                sender = RCSender(client)
                sender.start()
                while True:

                    message = client.receive()

                    if message is None:
                        raise ConnectionError(
                            "Onboard disconnected"
                        )

                    self.router.route(message)

            except Exception as e:

                logger.warning(e)

                time.sleep(2)

            finally:

                client.close()