from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QVBoxLayout,
)


class TelemetryPanel(QGroupBox):

    def __init__(self):
        super().__init__("Telemetry")

        layout = QVBoxLayout()

        self.lbl_connection = QLabel("🔴 Offline")
        self.lbl_mode = QLabel("Mode : ---")
        self.lbl_altitude = QLabel("Altitude : ---")
        self.lbl_speed = QLabel("Speed : ---")
        self.lbl_battery = QLabel("Battery : ---")

        layout.addWidget(self.lbl_connection)
        layout.addWidget(self.lbl_mode)
        layout.addWidget(self.lbl_altitude)
        layout.addWidget(self.lbl_speed)
        layout.addWidget(self.lbl_battery)

        self.setLayout(layout)
    def update(self, telemetry):

        if telemetry is None:
            return

        self.lbl_mode.setText(
            f"Mode: {telemetry.mode}"
        )

        self.lbl_altitude.setText(
            f"Altitude: {telemetry.altitude:.2f} m"
        )

        self.lbl_speed.setText(
            f"Speed: {telemetry.speed:.2f} m/s"
        )

        self.lbl_battery.setText(
            f"Battery: {telemetry.battery:.0f}%"
        )

        # if telemetry.connected:
        #     self.lbl_connection.setText("🟢 Connected")
        # else:
        #     self.lbl_connection.setText("🔴 Offline")
    
    def set_connection(self, connected: bool):

        if connected:
            self.lbl_connection.setText("🟢 Connected")
        else:
            self.lbl_connection.setText("🔴 Offline")


    def set_connecting(self):

        self.lbl_connection.setText("🟡 Connecting...")