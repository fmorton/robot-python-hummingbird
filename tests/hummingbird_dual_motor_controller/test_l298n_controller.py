from robot.hummingbird import Hummingbird
from robot.l298n_dual_motor_controller import L298nDualMotorController
from time import sleep


def move_left_motor(motors, speed):
    motors.move_left_motor(speed)
    sleep(1.0)


def move_right_motor(motors, speed):
    motors.move_right_motor(speed)
    sleep(1.0)


def test_l298n():
    hummingbird = Hummingbird()

    motors = L298nDualMotorController(hummingbird)

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
