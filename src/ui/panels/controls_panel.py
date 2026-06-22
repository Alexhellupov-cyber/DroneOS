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

    connect_clicked = Signal()

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

        self.btn_start = QPushButton("▶ Старт симулятора")
        self.btn_stop = QPushButton("■ Стоп симулятора")
        self.btn_restart = QPushButton("⟳ Рестарт симулятора")
        self.btn_connect = QPushButton("Подключиться")
        simulator_layout.addWidget(self.btn_start)
        simulator_layout.addWidget(self.btn_stop)
        simulator_layout.addWidget(self.btn_restart)
        simulator_layout.addWidget(self.btn_connect)

        simulator.setLayout(simulator_layout)

        # ---------------- Flight ----------------

        flight = QGroupBox("Flight")

        flight_layout = QVBoxLayout()
        
        self.btn_arm = QPushButton("Взвод")
        self.btn_takeoff = QPushButton("⬆ Взлет")
        self.btn_land = QPushButton("⬇ Посадка")
        self.btn_rtl = QPushButton("Возврат")

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
        self.btn_connect.clicked.connect(self.connect_clicked.emit)
        self.btn_arm.clicked.connect(self.arm_clicked.emit)
        self.btn_takeoff.clicked.connect(self.takeoff_clicked.emit)
        self.btn_land.clicked.connect(self.land_clicked.emit)
        self.btn_rtl.clicked.connect(self.rtl_clicked.emit)