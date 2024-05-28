import time;
import wiringpi;
from wiringpi import GPIO;

wiringpi.wiringPiSetup()
pwm_pin = 2
PWM_RANGE = 1024

wiringpi.softPwmCreate(pwm_pin, 0, PWM_RANGE)


def open_servo():
	wiringpi.softPwmWrite(pwm_pin, 7)
	wiringpi.delay(100)

def close_servo():
	wiringpi.softPwmWrite(pwm_pin, 19)
	wiringpi.delay(100)


def servo_move_to(pin, angle):
	pwm_value = int((angle / 180 * 51 ) + 51)
	wiringpi.softPwmWrite(pin, pwm_value)
	wiringpi.delay(10)


wiringpi.wiringPiSetup()
