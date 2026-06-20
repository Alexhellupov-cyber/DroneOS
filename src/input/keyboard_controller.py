import asyncio

from PySide6.QtCore import Qt


class KeyboardController:

    def __init__(self, drone):

        self.drone = drone

    def key_press(self, event):

        if event.isAutoRepeat():
            return

        if not self.drone.connected:
            return

        key = event.key()

        if key == Qt.Key_W:
            self.drone.set_forward(2.0)

        elif key == Qt.Key_S:
            self.drone.set_forward(-2.0)

        elif key == Qt.Key_A:
            self.drone.set_right(-2.0)

        elif key == Qt.Key_D:
            self.drone.set_right(2.0)

        elif key == Qt.Key_Q:
            self.drone.set_yaw(-45)

        elif key == Qt.Key_E:
            self.drone.set_yaw(45)

        elif key == Qt.Key_Space:
            self.drone.set_down(-1)

        elif key == Qt.Key_Control:
            self.drone.set_down(1)

        asyncio.create_task(
            self.drone.send_controls()
        )

    def key_release(self, event):

        if event.isAutoRepeat():
            return

        if not self.drone.connected:
            return

        key = event.key()

        if key in (Qt.Key_W, Qt.Key_S):
            self.drone.set_forward(0)

        elif key in (Qt.Key_A, Qt.Key_D):
            self.drone.set_right(0)

        elif key in (Qt.Key_Q, Qt.Key_E):
            self.drone.set_yaw(0)

        elif key in (Qt.Key_Space, Qt.Key_Control):
            self.drone.set_down(0)

        asyncio.create_task(
            self.drone.send_controls()
        )