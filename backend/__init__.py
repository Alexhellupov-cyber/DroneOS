import cv2
import os


class VideoCamera:

    def __init__(self):

        source = os.getenv("VIDEO_SOURCE")

        if source is None:
            if os.name == "nt":
                source = 0
            else:
                source = "/dev/video0"

        self.camera = cv2.VideoCapture(source)

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_FPS, 25)