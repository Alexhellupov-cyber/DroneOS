import asyncio
from mavsdk import System


class Telemetry:

    def __init__(self, drone: System):
        self.drone = drone

        self.mode = "---"
        self.altitude = 0.0
        self.speed = 0.0
        self.battery = 0.0
        self.latitude = 0.0
        self.longitude = 0.0
        self.satellites = 0
        self.connected = False
        self.in_air = False
        self.armed = False

    async def start(self):
        asyncio.create_task(self._watch_gps())
        asyncio.create_task(self._watch_mode())
        asyncio.create_task(self._watch_position())
        asyncio.create_task(self._watch_velocity())
        asyncio.create_task(self._watch_battery())
        asyncio.create_task(self._watch_armed())
        asyncio.create_task(self._watch_in_air())

    async def _watch_mode(self):
        async for mode in self.drone.telemetry.flight_mode():
            self.mode = str(mode)

    async def _watch_position(self):
        async for position in self.drone.telemetry.position():
            self.latitude = position.latitude_deg
            self.longitude = position.longitude_deg
            self.altitude = position.relative_altitude_m

            print("Altitude:", self.altitude)

    async def _watch_velocity(self):
        async for velocity in self.drone.telemetry.velocity_ned():

            self.speed = (
                velocity.north_m_s ** 2 +
                velocity.east_m_s ** 2 +
                velocity.down_m_s ** 2
            ) ** 0.5

    async def _watch_battery(self):
        async for battery in self.drone.telemetry.battery():

            self.battery = battery.remaining_percent

            print("Battery:", self.battery)

    async def _watch_armed(self):
        async for armed in self.drone.telemetry.armed():
            self.armed = armed

    async def _watch_in_air(self):
        async for in_air in self.drone.telemetry.in_air():
            self.in_air = in_air
    async def _watch_gps(self):

        async for gps in self.drone.telemetry.gps_info():

            self.satellites = gps.num_satellites