from src.core.controllers.application_controller import ApplicationController

controller = ApplicationController()

while True:

    packet = controller.update()

    print(packet.to_dict())