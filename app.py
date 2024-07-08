import servo_controller
import time
from flask import Flask

app = Flask(__name__)


@app.route('/move')
def hello_world():
    servo_controller.open_servo()
    time.sleep(1)
    servo_controller.close_servo()
    return 'OK'


# main driver function
if __name__ == '__main__':
    app.run()
