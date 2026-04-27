from robot.hummingbird import Hummingbird
from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from time import sleep

hummingbird = Hummingbird()

hummingbird_motors = HummingbirdL298nDualMotorDriver(hummingbird)

hummingbird_motors.move_left_motor(40)  # left motor forward
sleep(1.0)
hummingbird_motors.move_left_motor(0)  # stop left motor

hummingbird_motors.move_right_motor(-40)  # right motor backwards
sleep(1.0)

hummingbird_motors.move(50, 50)  # move both motors forward
sleep(1.0)

hummingbird_motors.stop()
