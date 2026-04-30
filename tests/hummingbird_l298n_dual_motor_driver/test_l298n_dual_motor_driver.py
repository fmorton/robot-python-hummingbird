from robot.hummingbird import Hummingbird
from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from robot.hummingbird_tb6612fng_dual_motor_driver import HummingbirdTb6612fngDualMotorDriver
from time import sleep


def move_left_motor(hummingbird_motors, speed):
    hummingbird_motors.move_left_motor(speed)
    sleep(1.0)


def move_right_motor(hummingbird_motors, speed):
    hummingbird_motors.move_right_motor(speed)
    sleep(1.0)


def test_l298n():
    hummingbird = Hummingbird()

    #hummingbird_motors = HummingbirdL298nDualMotorDriver(hummingbird)
    hummingbird_motors = HummingbirdTb6612fngDualMotorDriver(hummingbird)

    move_left_motor(hummingbird_motors, 50)
    move_left_motor(hummingbird_motors, 100)
    move_left_motor(hummingbird_motors, 25)
    move_left_motor(hummingbird_motors, 0)

    move_left_motor(hummingbird_motors, -50)
    move_left_motor(hummingbird_motors, -100)
    move_left_motor(hummingbird_motors, -25)
    move_left_motor(hummingbird_motors, -0)

    move_right_motor(hummingbird_motors, 50)
    move_right_motor(hummingbird_motors, 100)
    move_right_motor(hummingbird_motors, 25)
    move_right_motor(hummingbird_motors, 0)

    move_right_motor(hummingbird_motors, -50)
    move_right_motor(hummingbird_motors, -100)
    move_right_motor(hummingbird_motors, -25)
    move_right_motor(hummingbird_motors, -0)

    hummingbird_motors.move(100, 100)
    sleep(2.0)

    hummingbird_motors.move(-100, -100)
    sleep(2.0)

    hummingbird_motors.stop_all()

    assert True
