import json


class ConfigManager:

    def __init__(self,
                path="src/config/network.json"):

        self.path = path

        self.data = {}

        self.load()

    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(file)

    def get(self, *keys):

        value = self.data

        for key in keys:

            value = value[key]

        return value