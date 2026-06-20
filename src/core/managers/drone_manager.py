import asyncio

from src.core.services.connection_service import ConnectionService
from src.core.services.action_service import ActionService
from src.core.services.offboard_service import OffboardService
from src.core.services.telemetry_service import TelemetryService


class DroneManager:

    def __init__(self):

        self.connection = ConnectionService()
        self.action = ActionService()
        self.offboard = OffboardService()
        self.telemetry = TelemetryService()

        self.connected = False

    async def connect(self):

        if self.connected:
            return

        drone = await self.connection.connect()

        self.action.initialize(drone)
        self.offboard.initialize(drone)
        await self.telemetry.initialize(drone)

        self.connected = True

    # ==========================================
    # Flight
    # ==========================================

    async def arm(self):

        await self.connect()

        await self.action.arm()

    async def takeoff(self):

        await self.connect()

        await self.action.takeoff()

        await asyncio.sleep(1)

        await self.offboard.start()

    async def land(self):

        await self.connect()

        await self.action.land()

    async def rtl(self):

        await self.connect()

        await self.action.rtl()

    # ==========================================
    # Movement
    # ==========================================

    def set_forward(self, value):

        self.offboard.set_forward(value)

    def set_right(self, value):

        self.offboard.set_right(value)

    def set_down(self, value):

        self.offboard.set_down(value)

    def set_yaw(self, value):

        self.offboard.set_yaw(value)

    async def send_controls(self):

        await self.offboard.send()