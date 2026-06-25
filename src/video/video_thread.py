from PySide6.QtCore import QThread, Signal

from src.video.video_client import VideoClient


class VideoThread(QThread):

    frame_ready = Signal(object)

    def __init__(self, host):

        super().__init__()

        self.host = host

        self.running = True

    def run(self):

        client = VideoClient(self.host)

        while self.running:

            image = client.receive()

            if image:

                self.frame_ready.emit(image)

    def stop(self):

        self.running = False