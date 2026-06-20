from src.drivers.mavsdk.action import Action


class ActionService:

    def __init__(self):

        self.action = None


    def initialize(self, drone):

        self.action = Action(drone)


    async def arm(self):

        await self.action.arm()


    async def takeoff(self):

        await self.action.takeoff()


    async def land(self):

        await self.action.land()


    async def rtl(self):

        await self.action.rtl()