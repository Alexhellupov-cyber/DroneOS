from mavsdk import System


class DroneConnection:

    def __init__(self):

        self.drone = System(
            mavsdk_server_address="localhost",
            port=50051
        )

    async def connect(self):

        await self.drone.connect(
            system_address="udpin://0.0.0.0:14540"
        )

        async for state in self.drone.core.connection_state():

            if state.is_connected:

                return self.drone