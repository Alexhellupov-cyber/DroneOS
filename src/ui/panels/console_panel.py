from PySide6.QtWidgets import QTextEdit


class ConsolePanel(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setMaximumHeight(180)

        self.append("DroneOS v0.2 started...")

    def log(self, text):

        self.append(str(text))

        self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        )