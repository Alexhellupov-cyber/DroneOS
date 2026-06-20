from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QGridLayout,
    QGroupBox
)


class DroneOSPanel(QGroupBox):
    center_clicked = Signal()
    def __init__(self):

        super().__init__("DroneOS")

        layout = QGridLayout()

        self.status = QLabel("🔴 Не подключено")

        self.mode = QLabel("---")
        self.altitude = QLabel("---")
        self.speed = QLabel("---")
        self.battery = QLabel("---")
        self.gps = QLabel("---")
        self.satellites = QLabel("---")
        self.armed = QLabel("---")
        self.center_btn = QPushButton("🎯 На дрон")

        self.center_btn.clicked.connect(
            self.center_clicked.emit
        )
        for label in (
        self.mode,
        self.altitude,
        self.speed,
        self.battery,
        self.gps,
        self.satellites,
        self.armed
        ):
            label.setStyleSheet("""
                font-weight: bold;
                color: white;
            """)
        row = 0

        layout.addWidget(self.status, row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel("Режим полёта"), row, 0)
        layout.addWidget(self.mode, row, 1)

        row += 1
        layout.addWidget(QLabel("Высота"), row, 0)
        layout.addWidget(self.altitude, row, 1)

        row += 1
        layout.addWidget(QLabel("Скорость"), row, 0)
        layout.addWidget(self.speed, row, 1)

        row += 1
        layout.addWidget(QLabel("Батарея"), row, 0)
        layout.addWidget(self.battery, row, 1)

        row += 1
        layout.addWidget(QLabel("GPS"), row, 0)
        layout.addWidget(self.gps, row, 1)

        row += 1
        layout.addWidget(QLabel("Спутники"), row, 0)
        layout.addWidget(self.satellites, row, 1)

        row += 1
        layout.addWidget(QLabel("Состояние"), row, 0)
        layout.addWidget(self.armed, row, 1)
        row += 1

        layout.addWidget(
            self.center_btn,
            row,
            0,
            1,
            2
        )
        self.setLayout(layout)