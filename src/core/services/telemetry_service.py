from src.drivers.mavsdk.telemetry import Telemetry


class TelemetryService:

    def __init__(self):
        self.telemetry = None

    async def initialize(self, drone):

        self.telemetry = Telemetry(drone)
        await self.telemetry.start()

    @property
    def mode(self):
        if self.telemetry:
            return self.telemetry.mode
        return "---"

    @property
    def altitude(self):
        if self.telemetry:
            return self.telemetry.altitude
        return 0.0

    @property
    def speed(self):
        if self.telemetry:
            return self.telemetry.speed
        return 0.0

    @property
    def battery(self):
        if self.telemetry:
            return self.telemetry.battery
        return 0.0
    
    @property
    def latitude(self):
        if self.telemetry:
            return self.telemetry.latitude
        return 0.0


    @property
    def longitude(self):
        if self.telemetry:
            return self.telemetry.longitude
        return 0.0


    @property
    def satellites(self):
        if self.telemetry:
            return self.telemetry.satellites
        return 0

    @property
    def armed(self):
        if self.telemetry:
            return self.telemetry.armed
        return False

    @property
    def in_air(self):
        if self.telemetry:
            return self.telemetry.in_air
        return False