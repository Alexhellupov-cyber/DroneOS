import subprocess
import time

video = subprocess.Popen(["python", "backend/app.py"])
time.sleep(2)
server = subprocess.Popen(["python", "-m", "onboard.server"])

video.wait()
server.wait()