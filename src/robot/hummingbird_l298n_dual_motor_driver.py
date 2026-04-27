from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver


class HummingbirdL298nDualMotorDriver(HummingbirdDualMotorDriver):
    def move_left_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.left_polarity)

        if speed >= 0:
            self.robot.tri_led(1, speed, 0, 0)
        else:
            self.robot.tri_led(1, 0, abs(speed), 0)

    def move_right_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.right_polarity)

        if speed >= 0:
            self.robot.tri_led(2, 0, speed, 0)
        else:
            self.robot.tri_led(2, abs(speed), 0, 0)
