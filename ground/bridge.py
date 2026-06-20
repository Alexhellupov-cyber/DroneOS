from ground.logger import logger


class Bridge:

    def __init__(self):
        self.connections = []

    def add(self, connection):

        self.connections.append(connection)

        logger.info(
            f"Desktop connected ({len(self.connections)})"
        )

    def remove(self, connection):

        if connection in self.connections:
            self.connections.remove(connection)

        logger.info(
            f"Desktop disconnected ({len(self.connections)})"
        )

    def broadcast(self, message):

        logger.info(
            f"Broadcast to {len(self.connections)} desktop client(s)"
        )

        dead = []

        for connection in self.connections:

            try:

                logger.info(f"Sending: {message.type}")

                connection.send(message)

                logger.info("Message sent")

            except Exception as e:

                logger.error(f"Send failed: {e}")

                dead.append(connection)

        for connection in dead:

            self.remove(connection)