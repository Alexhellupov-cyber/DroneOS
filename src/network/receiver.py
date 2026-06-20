from threading import Thread

from src.core.events.event_bus import EventBus
from src.core.events.events import Events

from src.network.client import DroneOSClient


class DroneReceiver(Thread):

    def __init__(self):

        super().__init__(daemon=True)

        self.client = DroneOSClient()

    def run(self):

        self.client.connect()

        while True:

            message = self.client.receive()

            if message is None:
                break
            print("RECEIVED:", message)
            EventBus.emit(
                Events.TELEMETRY,
                message
            )