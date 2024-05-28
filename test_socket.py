import asyncio;
from websockets.sync.client import connect;

def test_open_close_servo() :
	with connect("ws://localhost:8765") as ws:
		ws.send("hi")
		message = ws.recv()
		print(message)


test_open_close_servo()
