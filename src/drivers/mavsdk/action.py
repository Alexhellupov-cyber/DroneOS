from mavsdk import System


class Action:

    def __init__(self, drone: System):
        self.drone = drone

    async def arm(self):
        print("🚀 Arming...")
        await self.drone.action.arm()
        print("✅ Drone Armed")

    async def disarm(self):
        print("🛑 Disarming...")
        await self.drone.action.disarm()
        print("✅ Drone Disarmed")

    async def takeoff(self):
        print("⬆️ Takeoff...")
        await self.drone.action.takeoff()
        print("✅ Takeoff command sent")

    async def land(self):
        print("⬇️ Landing...")
        await self.drone.action.land()
        print("✅ Landing command sent")

    async def rtl(self):
        print("🏠 Return To Launch...")
        await self.drone.action.return_to_launch()
        print("✅ RTL command sent")