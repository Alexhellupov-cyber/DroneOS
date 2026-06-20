from src.drivers.mavsdk.velocity import Velocity


class InputManager:

    def __init__(self):
        self.velocity = Velocity()

    def update(self, keys):

        self.velocity.update(keys)

        return self.velocity