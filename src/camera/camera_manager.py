from src.camera.frame import Frame


class CameraManager:

    def __init__(self):

        self.driver = None

        self.frame = Frame()

    async def start(self):

        if self.driver is None:
            return

        await self.driver.start()

    def get_frame(self):

        if self.driver is None:
            return self.frame

        return self.driver.frame