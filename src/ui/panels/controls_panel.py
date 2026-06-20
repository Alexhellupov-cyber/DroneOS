from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QPushButton,
    QVBoxLayout,
)


class ControlsPanel(QWidget):

    start_clicked = Signal()
    stop_clicked = Signal()
    restart_clicked = Signal()

    arm_clicked = Signal()
    takeoff_clicked = Signal()
    land_clicked = Signal()
    rtl_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # ---------------- Simulator ----------------

        simulator = QGroupBox("Simulator")

        simulator_layout = QVBoxLayout()

        self.btn_start = QPushButton("▶ Start")
        self.btn_stop = QPushButton("■ Stop")
        self.btn_restart = QPushButton("⟳ Restart")

        simulator_layout.addWidget(self.btn_start)
        simulator_layout.addWidget(self.btn_stop)
        simulator_layout.addWidget(self.btn_restart)

        simulator.setLayout(simulator_layout)

        # ---------------- Flight ----------------

        flight = QGroupBox("Flight")

        flight_layout = QVBoxLayout()

        self.btn_arm = QPushButton("🚀 ARM")
        self.btn_takeoff = QPushButton("⬆ TAKEOFF")
        self.btn_land = QPushButton("⬇ LAND")
        self.btn_rtl = QPushButton("🏠 RTL")

        flight_layout.addWidget(self.btn_arm)
        flight_layout.addWidget(self.btn_takeoff)
        flight_layout.addWidget(self.btn_land)
        flight_layout.addWidget(self.btn_rtl)

        flight.setLayout(flight_layout)

        layout.addWidget(simulator)
        layout.addWidget(flight)
        layout.addStretch()

        self.setLayout(layout)

        # Signals

        self.btn_start.clicked.connect(self.start_clicked.emit)
        self.btn_stop.clicked.connect(self.stop_clicked.emit)
        self.btn_restart.clicked.connect(self.restart_clicked.emit)

        self.btn_arm.clicked.connect(self.arm_clicked.emit)
        self.btn_takeoff.clicked.connect(self.takeoff_clicked.emit)
        self.btn_land.clicked.connect(self.land_clicked.emit)
        self.btn_rtl.clicked.connect(self.rtl_clicked.emit)