import os
import cv2


class VideoCamera:
    def __init__(self):
        source = os.getenv("VIDEO_SOURCE", "0")

        if source.isdigit():
            source = int(source)

        self.camera = cv2.VideoCapture(source)

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)