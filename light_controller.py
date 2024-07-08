import time;
# import wiringpi;
# from wiringpi import GPIO;

# wiringpi.wiringPiSetup()

RED_PIN = 1
GREEN_PIN = 2
BLUE_PIN = 3


def open_red() :
    # wiringpi.digitalWrite(RED_PIN, GPIO.HIGH)
    print("OPEN RED")

def close_red():
    # wiringpi.digitalWrite(RED_PIN, GPIO.LOW)
    print("CLOSE RED")

def open_green():
    # wiringpi.digitalWrite(GREEN_PIN, GPIO.HIGH)
    print("OPEN GREEN")

def close_green():
    # wiringpi.digitalWrite(GREEN_PIN, GPIO.LOW)
    print("CLOSE GREEN")

def open_blue():
    # wiringpi.digitalWrite(BLUE_PIN, GPIO.HIGH)
    print("OPEN BLUE")

def close_blue():
    # wiringpi.digitalWrite(BLUE_PIN, GPIO.LOW)
    print("CLOSE BLUE")

def light_handler(command):
    match command:
        case "STARTING":
            open_blue()
            time.sleep(1)
            close_blue()

        case "READY":
            open_blue()
            open_green()
            open_red()
            time.sleep(1)
            close_blue()
            close_green()
            close_red()

        case "PROCESSING":
            for i in range(5):
                open_blue()
                time.sleep(0.5)
                close_blue()

        case "ACCEPT":
            open_green()
            time.sleep(3)
            close_green()

        case "REJECT":
            open_red()
            time.sleep(3)
            close_red()
# wiringpi.wiringPiSetup()
