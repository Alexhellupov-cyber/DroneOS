import cv2


class VideoCamera:
    def __init__(self, source=0):
        self.camera = cv2.VideoCapture(1)

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_FPS, 25)

    def get_frame(self):
        success, frame = self.camera.read()

        if not success:
            return None

        _, jpeg = cv2.imencode(".jpg", frame)

        return jpeg.tobytes()

    def release(self):
        self.camera.release()