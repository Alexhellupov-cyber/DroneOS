from abc import ABC, abstractmethod


class BaseTransport(ABC):

    @abstractmethod
    def connect(self):
        """Установить соединение"""
        pass

    @abstractmethod
    def disconnect(self):
        """Разорвать соединение"""
        pass

    @abstractmethod
    def send(self, message):
        """Отправить сообщение"""
        pass

    @abstractmethod
    def receive(self):
        """Получить сообщение"""
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """Проверить соединение"""
        pass