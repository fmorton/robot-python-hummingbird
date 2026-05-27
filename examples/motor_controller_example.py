from robot.hummingbird import Hummingbird
from robot.l298n_dual_motor_controller import L298nDualMotorController
from time import sleep

hummingbird = Hummingbird()

motors = L298nDualMotorController(hummingbird)

motors.move_left_motor(40)  # left motor forward
sleep(1.0)
motors.move_left_motor(0)  # stop left motor

motors.move_right_motor(-40)  # right motor backwards
sleep(1.0)

motors.move(50, 50)  # move both motors forward
sleep(1.0)

motors.stop()
