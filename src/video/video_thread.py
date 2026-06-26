from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

import cv2


class VideoThread(QThread):

    frame_ready = Signal(QImage)

    def __init__(self, ip):
        super().__init__()

        self.running = True

        self.url = f"http://{ip}:5000/video"

    def run(self):

        cap = cv2.VideoCapture(self.url)

        while self.running:

            ok, frame = cap.read()

            if not ok:
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = rgb.shape

            image = QImage(
                rgb.data,
                w,
                h,
                ch * w,
                QImage.Format_RGB888,
            ).copy()

            self.frame_ready.emit(image)

        cap.release()

    def stop(self):

        self.running = False

        self.wait()