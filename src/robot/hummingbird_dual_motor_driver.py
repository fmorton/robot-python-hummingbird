from collections.abc import Sequence


class HummingbirdDualMotorDriver:
    MINIMUM_SPEED = 30

    def __init__(self, hummingbird, minimum_speed=None):
        self.minimum_speed = minimum_speed

        if minimum_speed is None:
            self.minimum_speed = self.MINIMUM_SPEED

        self.left_polarity = 1
        self.right_polarity = 1

        self.robot = hummingbird

    def reverse_left_polarity(self):
        self.left_polarity = -self.left_polarity

    def reverse_right_polarity(self):
        self.right_polarity = -self.right_polarity

    def reverse_polarity(self):
        reverse_left_polarity()
        reverse_right_polarity()

    def adjust_speed_for_polarity(self, speed, multiplier):
        return speed * multiplier

    def move(self, left_speed, right_speed=None):
        if isinstance(left_speed, Sequence):
            left_speed, right_speed = left_speed

        self.move_left_motor(left_speed)
        self.move_right_motor(right_speed)

    def move_left_motor(self, speed):
        pass

    def move_right_motor(self, speed):
        pass

    def stop(self):
        self.robot.tri_led(1, 0, 0, 0)
        self.robot.tri_led(2, 0, 0, 0)

    def stop_all(self):
        self.stop()
        self.robot.stop_all()
