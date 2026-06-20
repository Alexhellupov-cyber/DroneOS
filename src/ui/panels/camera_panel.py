from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class CameraPanel(QLabel):

    def __init__(self):
        super().__init__("FPV CAMERA")

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumHeight(600)

        self.setStyleSheet("""
        background:#111;
        border:2px solid #444;
        color:#888;
        font-size:28px;
        """)

    def set_frame(self, image: QImage):

        pixmap = QPixmap.fromImage(image)

        self.setPixmap(
            pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    def clear(self):

        self.setText("FPV CAMERA")