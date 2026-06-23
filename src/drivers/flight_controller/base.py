from abc import ABC, abstractmethod


class FlightController(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def arm(self):
        pass

    @abstractmethod
    def disarm(self):
        pass

    @abstractmethod
    def send_rc(
        self,
        roll,
        pitch,
        yaw,
        throttle,
        aux1=1000,
        aux2=1000,
        aux3=1000,
        aux4=1000,
    ):
        pass

    @abstractmethod
    def get_telemetry(self):
        pass