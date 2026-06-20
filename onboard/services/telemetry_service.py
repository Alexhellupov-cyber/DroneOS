import socket
import time

try:
    import psutil
except ImportError:
    psutil = None


class TelemetryService:

    def collect(self):

        data = {
            "hostname": socket.gethostname(),
            "timestamp": int(time.time()),
            "uptime": 0,
            "cpu": 0,
            "memory": 0,
        }

        if psutil:

            data["uptime"] = int(time.time() - psutil.boot_time())
            data["cpu"] = psutil.cpu_percent(interval=0)
            data["memory"] = psutil.virtual_memory().percent

        return data