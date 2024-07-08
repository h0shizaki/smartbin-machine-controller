import light_controller
import servo_controller
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/move')
def move():
    servo_controller.open_servo()
    time.sleep(1)
    servo_controller.close_servo()
    return jsonify({'message': 'OK'})


@app.route('/light', methods=['PUT'])
def update_light():
    data = request.json
    print(data["data"])
    light_controller.light_handler(data["data"])
    return jsonify(data)


# main driver function
if __name__ == '__main__':
    app.run()
