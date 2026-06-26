from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

import cv2
import numpy as np
import requests


class VideoThread(QThread):

    frame_ready = Signal(QImage)

    def __init__(self, ip):
        super().__init__()

        self.running = True
        self.url = f"http://{ip}:5000/video"

    def run(self):

        stream = requests.get(self.url, stream=True)

        buffer = bytes()

        for chunk in stream.iter_content(chunk_size=4096):

            if not self.running:
                break

            buffer += chunk

            a = buffer.find(b'\xff\xd8')
            b = buffer.find(b'\xff\xd9')

            if a != -1 and b != -1:

                jpg = buffer[a:b+2]

                buffer = buffer[b+2:]

                frame = cv2.imdecode(
                    np.frombuffer(jpg, dtype=np.uint8),
                    cv2.IMREAD_COLOR
                )

                if frame is None:
                    continue

                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                h, w, ch = rgb.shape

                image = QImage(
                    rgb.data,
                    w,
                    h,
                    ch * w,
                    QImage.Format_RGB888
                ).copy()

                self.frame_ready.emit(image)

    def stop(self):

        self.running = False
        self.wait()