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

    def get_frame(self):
        success, frame = self.camera.read()

        if not success:
            return None

        _, buffer = cv2.imencode(".jpg", frame)

        return buffer.tobytes()

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()