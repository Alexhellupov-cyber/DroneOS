import time

from corelib.config import ONBOARD_BIND_HOST, ONBOARD_PORT
from corelib.logger import get_logger
from corelib.messages import telemetry
from corelib.network import DroneServer

from onboard.services.telemetry_service import TelemetryService

logger = get_logger()


def main():

    telemetry_service = TelemetryService()

    server = DroneServer(
        ONBOARD_BIND_HOST,
        ONBOARD_PORT
    )

    while True:

        client, address = server.accept()

        logger.info(f"Ground connected: {address}")

        try:

            while True:

                message = telemetry(
                    telemetry_service.collect()
                )

                client.send(message)

                time.sleep(1)

        except Exception as e:

            logger.warning(f"Connection closed: {e}")

        finally:

            client.close()


if __name__ == "__main__":
    main()