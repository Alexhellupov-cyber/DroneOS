import os
import signal
import subprocess
import threading
import time

from PySide6.QtCore import QObject, Signal


class ProcessManager(QObject):

    log = Signal(str)
    started = Signal()
    stopped = Signal()

    def __init__(self):
        super().__init__()
        self.mavsdk = None
        self.process = None
        self.mavsdk = None
        self.project_dir = os.path.expanduser(
            "~/Projects/PX4-Autopilot"
        )

    def start_px4(self):

        if self.process and self.process.poll() is None:
            self.log.emit("PX4 already running.")
            return

        self.stop_px4()

        time.sleep(2)

        self.log.emit("Starting PX4 SITL...")

        cmd = f"""
        unset VIRTUAL_ENV
        export PATH=/usr/bin:/bin:/usr/local/bin:$PATH
        cd "{self.project_dir}"
        exec make px4_sitl gz_x500_vision
        """

        self.process = subprocess.Popen(
            ["bash", "-lc", cmd],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        threading.Thread(
            target=self._reader,
            daemon=True
        ).start()

        self.started.emit()
        time.sleep(5)

        self.log.emit("Starting MAVSDK Server...")
        mavsdk_server = os.path.expanduser(
            "~/Projects/DronOS/.venv/lib/python3.12/site-packages/mavsdk/bin/mavsdk_server"
        )
        self.mavsdk = subprocess.Popen(
            [
                mavsdk_server,
                "-p",
                "50051",
                "udp://:14540"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        print("PID =", self.mavsdk.pid)

        time.sleep(1)

        print("EXIT =", self.mavsdk.poll())

        threading.Thread(
            target=self._reader_mavsdk,
            daemon=True,
        ).start()

    def stop_px4(self):

        self.log.emit("Stopping PX4...")

        if self.process and self.process.poll() is None:
            try:
                self.process.send_signal(signal.SIGINT)
                time.sleep(1)
                self.process.kill()
            except Exception:
                pass

        os.system("pkill -9 -f px4")
        os.system("pkill -9 -f gz")
        os.system("pkill -9 -f ruby")
        os.system("pkill -9 -f mavsdk_server")

        time.sleep(2)
        if self.mavsdk and self.mavsdk.poll() is None:

            self.mavsdk.kill()

        self.mavsdk = None
        self.process = None

        self.stopped.emit()

    def restart_px4(self):

        self.stop_px4()
        self.start_px4()

    def _reader(self):

        for line in self.process.stdout:

            line = line.rstrip()

            if line:
                self.log.emit(line)
    def _reader_mavsdk(self):

        for line in self.mavsdk.stdout:

            line = line.rstrip()

            if line:
                self.log.emit("[MAVSDK] " + line)