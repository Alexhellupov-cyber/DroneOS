from src.drivers.mavsdk.offboard import OffboardController


class OffboardService:

    def __init__(self):

        self.offboard = None

    def initialize(self, drone):

        self.offboard = OffboardController(drone)

    async def start(self):

        await self.offboard.start()

    async def stop(self):

        await self.offboard.stop()

    async def send(self):

        await self.offboard.send()

    def set_forward(self, value):

        self.offboard.velocity.forward = value

    def set_right(self, value):

        self.offboard.velocity.right = value

    def set_down(self, value):

        self.offboard.velocity.down = value

    def set_yaw(self, value):

        self.offboard.velocity.yaw = value