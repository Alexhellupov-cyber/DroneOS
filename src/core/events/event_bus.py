class EventBus:

    _listeners = {}


    @classmethod
    def subscribe(cls, event, callback):

        if event not in cls._listeners:
            cls._listeners[event] = []

        cls._listeners[event].append(callback)


    @classmethod
    def emit(cls, event, data=None):

        if event not in cls._listeners:
            return

        for callback in cls._listeners[event]:
            callback(data)