import time;
import wiringpi;
from wiringpi import GPIO;

wiringpi.wiringPiSetup()

RED_PIN = 5
GREEN_PIN = 7
BLUE_PIN = 8


def open_red():
    wiringpi.digitalWrite(RED_PIN, GPIO.HIGH)


def close_red():
    wiringpi.digitalWrite(RED_PIN, GPIO.LOW)


def open_green():
    wiringpi.digitalWrite(GREEN_PIN, GPIO.HIGH)


def close_green():
    wiringpi.digitalWrite(GREEN_PIN, GPIO.LOW)


def open_blue():
    wiringpi.digitalWrite(BLUE_PIN, GPIO.HIGH)


def close_blue():
    wiringpi.digitalWrite(BLUE_PIN, GPIO.LOW)


def light_handler(command):
    if command == "STARTING":
        open_blue()
        time.sleep(1)
        close_blue()

    if command == "READY":
        open_blue()
        open_green()
        open_red()
        time.sleep(1)
        close_blue()
        close_green()
        close_red()

    if command == "PROCESSING":
        for i in range(5):
            open_blue()
            time.sleep(0.5)
            close_blue()

    if command == "ACCEPT":
        open_green()
        time.sleep(3)
        close_green()

    if command == "REJECT":
        open_red()
        time.sleep(3)
        close_red()


wiringpi.wiringPiSetup()
