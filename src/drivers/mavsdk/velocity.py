from src.config.settings import Settings


class Velocity:

    def __init__(self):

        self.forward = 0.0
        self.right = 0.0
        self.down = 0.0
        self.yaw = 0.0

    def smooth(self, value):

        if value > 0:
            value = max(0.0, value - Settings.DECELERATION)

        elif value < 0:
            value = min(0.0, value + Settings.DECELERATION)

        return value

    def update(self, keys):

        # ---------- Forward ----------

        if keys["forward"]:
            self.forward = min(
                self.forward + Settings.ACCELERATION,
                Settings.MAX_FORWARD
            )

        elif keys["back"]:
            self.forward = max(
                self.forward - Settings.ACCELERATION,
                -Settings.MAX_FORWARD
            )

        else:
            self.forward = self.smooth(self.forward)

        # ---------- Right ----------

        if keys["right"]:
            self.right = min(
                self.right + Settings.ACCELERATION,
                Settings.MAX_RIGHT
            )

        elif keys["left"]:
            self.right = max(
                self.right - Settings.ACCELERATION,
                -Settings.MAX_RIGHT
            )

        else:
            self.right = self.smooth(self.right)

        # ---------- Vertical ----------

        if keys["up"] or keys["takeoff"]:
            self.down = max(
                self.down - Settings.ACCELERATION,
                -Settings.MAX_VERTICAL
            )

        elif keys["down"]:
            self.down = min(
                self.down + Settings.ACCELERATION,
                Settings.MAX_VERTICAL
            )

        else:
            self.down = self.smooth(self.down)

        # ---------- Yaw ----------

        if keys["yaw_right"]:
            self.yaw = min(
                self.yaw + 2,
                Settings.MAX_YAW
            )

        elif keys["yaw_left"]:
            self.yaw = max(
                self.yaw - 2,
                -Settings.MAX_YAW
            )

        else:
            self.yaw = self.smooth(self.yaw)