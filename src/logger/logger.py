from datetime import datetime


class Logger:
    def info(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] [INFO] {message}")

    def warning(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] [WARNING] {message}")

    def error(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] [ERROR] {message}")