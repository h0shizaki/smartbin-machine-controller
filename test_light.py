import time;
import wiringpi;
from wiringpi import GPIO;

wiringpi.wiringPiSetup()
RED_PIN = 5
GREEN_PIN = 7
BLUE_PIN = 8

for i in range(4):
  wiringpi.digitalWrite(GREEN_PIN, GPIO.HIGH)
  wiringpi.digitalWrite(BLUE_PIN, GPIO.HIGH)
  wiringpi.digitalWrite(RED_PIN, GPIO.HIGH)
  time.sleep(3)
  wiringpi.digitalWrite(GREEN_PIN, GPIO.LOW)
  wiringpi.digitalWrite(BLUE_PIN, GPIO.LOW)
  wiringpi.digitalWrite(RED_PIN, GPIO.LOW)
