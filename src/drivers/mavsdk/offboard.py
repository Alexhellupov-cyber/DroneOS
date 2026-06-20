import asyncio

from mavsdk import System
from mavsdk.offboard import VelocityBodyYawspeed, OffboardError

from src.drivers.mavsdk.velocity import Velocity


class OffboardController:

    def __init__(self, drone: System):

        self.drone = drone
        self.velocity = Velocity()
        self.running = False
        self._task = None

    async def start(self):

        print("Starting Offboard...")

        try:

            await self.send()

            await self.drone.offboard.start()

            self.running = True

            if self._task is None or self._task.done():
                self._task = asyncio.create_task(self.loop())

        except OffboardError as e:

            print(f"❌ Offboard ERROR: {e}")

        except Exception as e:

            print(f"❌ {e}")

    async def stop(self):

        self.running = False

        try:
            await self.drone.offboard.stop()
        except OffboardError:
            pass

    async def loop(self):

        print("🚀 Offboard loop started")

        while self.running:

            try:

                await self.send()

            except Exception as e:

                print(f"❌ Offboard send error: {e}")

            await asyncio.sleep(0.005)

    async def send(self):

        await self.drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(
                self.velocity.forward,
                self.velocity.right,
                self.velocity.down,
                self.velocity.yaw
            )
        )