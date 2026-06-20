import os
import subprocess
import time


class Simulator:

    def __init__(self, logger=None):

        self.logger = logger
        self.process = None

        self.px4_dir = os.path.expanduser(
            "~/Projects/PX4-Autopilot"
        )

    def log(self, text):

        if self.logger:
            self.logger(text)
        else:
            print(text)

    def start(self):

        if self.process and self.process.poll() is None:
            self.log("PX4 already running.")
            return

        self.log("Starting PX4 SITL...")

        env = os.environ.copy()

        # Убираем виртуальное окружение DroneOS
        env.pop("VIRTUAL_ENV", None)

        env["PATH"] = "/usr/bin:/bin:/usr/local/bin"

        self.process = subprocess.Popen(
            [
                "bash",
                "-lc",
                "unset VIRTUAL_ENV && export PATH=/usr/bin:/bin:$PATH && make px4_sitl gz_x500"
            ],
            cwd=self.px4_dir,
            env=env
        )

    def stop(self):

        self.log("Stopping PX4...")

        os.system("pkill -f bin/px4")
        os.system("pkill -f gz")
        os.system("pkill -f mavsdk_server")

        self.process = None

    def restart(self):

        self.stop()

        time.sleep(2)

        self.start()