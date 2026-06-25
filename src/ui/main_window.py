import asyncio
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from corelib import message
from src.simulator.process_manager import ProcessManager

from src.core.managers.drone_manager import DroneManager
from src.input.keyboard_controller import KeyboardController

from src.core.events.event_bus import EventBus
from src.core.events.events import Events

from src.network.receiver import DroneReceiver

from src.ui.panels.droneos_panel import DroneOSPanel
from src.ui.panels.map_panel import MapPanel
from src.ui.panels.telemetry_panel import TelemetryPanel
from src.ui.panels.camera_panel import CameraPanel
from src.ui.panels.console_panel import ConsolePanel
from src.ui.panels.controls_panel import ControlsPanel

from src.network.network_manager import NetworkManager
from src.network.router import MessageRouter

from src.services.telemetry_service import TelemetryService

from src.core.controllers.application_controller import ApplicationController

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.connected = False
        self.setup_window()

        self.build_ui()

        self.create_managers()

        self.connect_events()

        self.create_timers()
    
    def setup_window(self):

        self.setWindowTitle("DroneOS v0.2")

        self.resize(1600, 900)

        self.setFocusPolicy(Qt.StrongFocus)

        # self.setFocus()
    
    def build_ui(self):

        root = QHBoxLayout()

        # ======================================
        # LEFT
        # ======================================

        left = QVBoxLayout()

        self.droneos_panel = DroneOSPanel()
        self.map_panel = MapPanel()
        left.addWidget(self.droneos_panel)
        left.addWidget(self.map_panel, 1)

        # ======================================
        # CENTER
        # ======================================

        center = QVBoxLayout()

        self.camera_panel = CameraPanel()

        center.addWidget(
            self.camera_panel
        )

        self.console_panel = ConsolePanel()

        self.console_panel.log(
            "DroneOS v0.2 started..."
        )

        center.addWidget(
            self.console_panel
        )

        # ======================================
        # RIGHT
        # ======================================

        right = QVBoxLayout()

        self.controls_panel = ControlsPanel()

        right.addWidget(
            self.controls_panel
        )

        # ======================================
        # LAYOUT
        # ======================================

        root.addLayout(left, 1)
        root.addLayout(center, 3)
        root.addLayout(right, 1)

        self.setLayout(root)

        # ======================================
        # STYLE
        # ======================================

        self.setStyleSheet("""

        QWidget{
            background:#1E1E1E;
            color:white;
            font-size:14px;
        }

        QGroupBox{
            border:1px solid #444;
            border-radius:8px;
            margin-top:12px;
            padding-top:12px;
            font-weight:bold;
        }

        QPushButton{
            background:#1976D2;
            border:none;
            border-radius:6px;
            padding:12px;
            font-weight:bold;
            color:white;
        }

        QPushButton:hover{
            background:#2196F3;
        }

        QTextEdit{
            background:#101010;
            border:1px solid #333;
        }

        QLabel{
            padding:4px;
        }

        """)
    def create_managers(self):

        self.process = ProcessManager()

        self.drone = DroneManager()
        
        self.keyboard = KeyboardController(
            self.drone
        )

        self.network = NetworkManager()

        self.router = MessageRouter()
        self.telemetry_service = TelemetryService(self)
        self.controller = ApplicationController(
            self.network
        )

    def create_timers(self):

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_loop
        )

        self.timer.start(10)
        pass

    def update_loop(self):

        if self.connected:
            print("SEND")
            self.controller.update()

        self.update_telemetry()
    
    def connect_events(self):

        # =============================
        # EventBus
        # =============================

        EventBus.subscribe(
            Events.LOG,
            self.console_panel.log
        )

        EventBus.subscribe(
            Events.TELEMETRY,
            self.update_system_telemetry
        )

        self.droneos_panel.center_clicked.connect(
            self.map_panel.center_on_drone
        )

        # =============================
        # Controls
        # =============================

        self.controls_panel.start_clicked.connect(
            self.start_sim
        )

        self.controls_panel.stop_clicked.connect(
            self.stop_sim
        )

        self.controls_panel.restart_clicked.connect(
            self.restart_sim
        )

        self.controls_panel.connect_clicked.connect(
            self.connect_network
        )

        self.controls_panel.arm_clicked.connect(
            self.arm_drone
        )

        self.controls_panel.takeoff_clicked.connect(
            self.takeoff_drone
        )

        self.controls_panel.land_clicked.connect(
            self.land_drone
        )

        self.controls_panel.rtl_clicked.connect(
            self.rtl_drone
        )

        self.router.register(
            "telemetry",
            self.telemetry_service.handle
        )
    # =====================================================
    # Telemetry
    # =====================================================

    def update_telemetry(self):

        if self.drone.telemetry.telemetry is None:
            return

        telemetry = self.drone.telemetry

        self.map_panel.update_position(
            telemetry.latitude,
            telemetry.longitude
        )

        self.droneos_panel.status.setText("🟢 Подключено")

        self.droneos_panel.mode.setText(
            f"Режим полёта : {telemetry.mode}"
        )

        self.droneos_panel.altitude.setText(
            f"Высота : {telemetry.altitude:.2f} м"
        )

        self.droneos_panel.speed.setText(
            f"Скорость : {telemetry.speed:.2f} м/с"
        )

        self.droneos_panel.battery.setText(
            f"Батарея : {telemetry.battery:.0%}"
        )

        self.droneos_panel.gps.setText(
            f"GPS : {telemetry.latitude:.6f}, {telemetry.longitude:.6f}"
        )

        self.droneos_panel.satellites.setText(
            f"Спутники : {telemetry.satellites}"
        )

        self.droneos_panel.armed.setText(
            "Состояние : Взведён" if telemetry.armed else "Состояние : Не взведён"
        )
    
    # =====================================================
    # Simulator
    # =====================================================

    def start_sim(self):

        EventBus.emit(
            Events.LOG,
            "▶ Starting PX4..."
        )

        self.droneos_panel.status.setText(
            "🟡 Подключение..."
        )

        self.process.start_px4()

        QTimer.singleShot(
            10000,
            lambda: asyncio.create_task(
                self.connect_drone()
            )
        )


    def stop_sim(self):

        EventBus.emit(
            Events.LOG,
            "■ Stopping PX4..."
        )

        self.process.stop_px4()


    def restart_sim(self):

        EventBus.emit(
            Events.LOG,
            "⟳ Restarting PX4..."
        )

        self.process.restart_px4()
    
    # =====================================================
    # Flight
    # =====================================================

    def arm_drone(self):

        asyncio.create_task(
            self._arm_task()
        )


    async def _arm_task(self):

        print("1")

        try:

            print("2")

            EventBus.emit(
                Events.LOG,
                "🚀 ARM"
            )

            print("3")

            await self.drone.arm()

            print("4")

        except Exception:

            import traceback
            traceback.print_exc()


    def takeoff_drone(self):

        EventBus.emit(
            Events.LOG,
            "⬆ TAKEOFF"
        )

        asyncio.create_task(
            self.drone.takeoff()
        )


    def land_drone(self):

        EventBus.emit(
            Events.LOG,
            "⬇ LAND"
        )

        asyncio.create_task(
            self.drone.land()
        )


    def rtl_drone(self):

        EventBus.emit(
            Events.LOG,
            "🏠 RTL"
        )

        asyncio.create_task(
            self.drone.rtl()
        )

    def connect_network(self):

        self.console_panel.log(
            "Подключение к Ground..."
        )

        if self.network.connect("tcp"):

            self.connected = True

            self.console_panel.log(
                "TCP подключен"
            )

            self.network.subscribe(
                self.on_message
            )

        else:

            self.console_panel.log(
                "Ошибка подключения"
            )

    # =====================================================
    # Keyboard
    # =====================================================

    def keyPressEvent(self, event):

        self.keyboard.key_press(event)


    def keyReleaseEvent(self, event):

        self.keyboard.key_release(event)

    # =====================================================
    # Connection
    # =====================================================

    async def connect_drone(self):

        EventBus.emit(
            Events.LOG,
            "Connecting to PX4..."
        )

        try:

            await self.drone.connect()

            self.droneos_panel.status.setText("🟢 Подключено")

            EventBus.emit(
                Events.LOG,
                "✅ Connected to PX4"
            )

        except Exception as e:

            self.droneos_panel.status.setText("🔴 Нет соединения")

            EventBus.emit(
                Events.LOG,
                f"❌ Connection failed: {e}"
            )

    def on_message(self, message):

        self.router.route(message)

    def update_system_telemetry(self, payload):

        self.console_panel.log(
            "Telemetry received"
        )

        self.droneos_panel.status.setText(
            f"🟢 {payload['hostname']}"
        )