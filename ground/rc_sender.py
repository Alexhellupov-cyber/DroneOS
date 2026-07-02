import threading
import time

from corelib.message import Message
from src.input.usb_input import USBInput


class RCSender(threading.Thread):

    def __init__(self, client):

        super().__init__(daemon=True)

        self.client = client
        self.input = USBInput()

        self.running = True

    def run(self):

        print("RC Sender started")

        while self.running:

            packet = self.input.update()

            try:

                self.client.send(
                    Message(
                        "rc",
                        packet.__dict__
                    )
                )

            except Exception as e:

                print("RC SEND:", e)

            time.sleep(0.004)