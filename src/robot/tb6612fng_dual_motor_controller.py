from robot.dual_motor_controller import DualMotorController


class Tb6612fngDualMotorController(DualMotorController):
    def move_left_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.left_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.tri_led(1, 0, 0, 0)
        elif speed > 0:
            self.robot.tri_led(1, abs(speed), 100, 0)
        else:
            self.robot.tri_led(1, abs(speed), 0, 100)

    def move_right_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.right_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.tri_led(2, 0, 0, 0)
        elif speed > 0:
            self.robot.tri_led(2, 0, 100, abs(speed))
        else:
            self.robot.tri_led(2, 100, 0, abs(speed))
