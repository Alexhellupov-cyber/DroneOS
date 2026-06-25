import time
from src.drivers.crsf.driver import CRSFDriver
from src.input.rc_packet import RCPacket
from corelib.config import ONBOARD_BIND_HOST, ONBOARD_PORT
from corelib.logger import get_logger
from corelib.messages import telemetry
from corelib.network import DroneServer

from onboard.services.telemetry_service import TelemetryService

logger = get_logger()


def main():

    telemetry_service = TelemetryService()
    crsf = CRSFDriver()
    server = DroneServer(
        ONBOARD_BIND_HOST,
        ONBOARD_PORT
    )

    while True:

        client, address = server.accept()

        logger.info(f"Ground connected: {address}")

        try:

            while True:

                incoming = client.receive_nowait()

                if incoming:

                    logger.info(
                        f"GROUND -> {incoming}"
                    )

                    if incoming.type == "rc":

                        packet = RCPacket(
                            **incoming.payload
                        )

                        crsf.send(packet)

                outgoing = telemetry(
                    telemetry_service.collect()
                )

                client.send(outgoing)

                time.sleep(0.02)

        except Exception as e:

            logger.warning(f"Connection closed: {e}")

        finally:

            client.close()


if __name__ == "__main__":
    main()