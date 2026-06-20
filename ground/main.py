import threading

from ground.bridge import Bridge
from ground.desktop_server import DesktopServer
from ground.drone_client import GroundDroneClient
from ground.router import Router


def main():

    bridge = Bridge()

    router = Router(bridge)

    desktop = DesktopServer(bridge)

    drone = GroundDroneClient(router)

    threading.Thread(
        target=desktop.start,
        daemon=True
    ).start()

    drone.start()


if __name__ == "__main__":
    main()