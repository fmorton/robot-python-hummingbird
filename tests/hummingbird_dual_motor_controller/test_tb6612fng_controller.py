from robot.hummingbird import Hummingbird
from robot.tb6612fng_dual_motor_controller import Tb6612fngDualMotorController
from time import sleep


def move_left_motor(motors, speed):
    motors.move_left_motor(speed)
    sleep(1.0)


def move_right_motor(motors, speed):
    motors.move_right_motor(speed)
    sleep(1.0)


def test_tb6612fng():
    hummingbird = Hummingbird()

    motors = Tb6612fngDualMotorController(hummingbird)

    move_left_motor(motors, 50)
    move_left_motor(motors, 100)
    move_left_motor(motors, 25)
    move_left_motor(motors, 0)

    move_left_motor(motors, -50)
    move_left_motor(motors, -100)
    move_left_motor(motors, -25)
    move_left_motor(motors, -0)

    move_right_motor(motors, 50)
    move_right_motor(motors, 100)
    move_right_motor(motors, 25)
    move_right_motor(motors, 0)

    move_right_motor(motors, -50)
    move_right_motor(motors, -100)
    move_right_motor(motors, -25)
    move_right_motor(motors, -0)

    motors.move(100, 100)
    sleep(2.0)

    motors.move(-100, -100)
    sleep(2.0)

    motors.stop_all()

    assert True
