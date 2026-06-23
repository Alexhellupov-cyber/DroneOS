from src.core.events.event_bus import EventBus
from src.core.events.events import Events

class TelemetryService:

    def __init__(self, window):

        self.window = window

    def handle(self, message):

        EventBus.emit(
            Events.TELEMETRY,
            message.payload
        )
