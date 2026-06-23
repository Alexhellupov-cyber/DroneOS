class MessageRouter:

    def __init__(self):

        self.handlers = {}

    def register(self, message_type, handler):

        self.handlers[message_type] = handler

    def route(self, message):

        handler = self.handlers.get(message.type)

        if handler:

            handler(message)

        else:

            print(f"No handler for '{message.type}'")