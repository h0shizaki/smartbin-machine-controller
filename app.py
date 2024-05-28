import servo_controller;
import time;
import asyncio;
import websockets;

async def servo_control_handler(ws):
	try:
		servo_controller.open_servo()
		time.sleep(1)
		servo_controller.close_servo()
		await ws.send("OK")
	except:
		print("FAILED")


start_server = websockets.serve(servo_control_handler, "0.0.0.0", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
