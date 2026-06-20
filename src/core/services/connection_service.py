from src.drivers.mavsdk.connection import DroneConnection


class ConnectionService:

    def __init__(self):

        self.connection = DroneConnection()

        self.drone = None

        self.connected = False


    async def connect(self):

        if self.connected:
            return self.drone

        self.drone = await self.connection.connect()

        self.connected = True

        return self.drone