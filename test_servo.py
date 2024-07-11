import wiringpi;
from wiringpi import GPIO;

wiringpi.wiringPiSetup()
pwm_pin = 2
PWM_RANGE = 1024
wiringpi.softPwmCreate(pwm_pin, 0, PWM_RANGE)

wiringpi.softPwmWrite(pwm_pin, 7)
wiringpi.delay(100)
wiringpi.softPwmWrite(pwm_pin, 19)
wiringpi.delay(100)
