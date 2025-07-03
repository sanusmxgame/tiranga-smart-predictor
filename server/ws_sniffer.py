import websocket
import json
import threading
from hash_decoder import decode_hash
from database import save_round

WS_URL = "wss://tirangagame.top/socket.io/?EIO=4&transport=websocket"

def on_message(ws, message):
    try:
        data = json.loads(message)
        if "hash" in data:
            decoded = decode_hash(data["hash"])
            round_data = data | decoded
            save_round(round_data)
            print(f"Round saved: {round_data}")
    except Exception as e:
        print(f"Error parsing WebSocket message: {e}")

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connected")

def capture_websocket():
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(WS_URL,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close,
                                 on_open=on_open)
    ws.run_forever()

if __name__ == "__main__":
    capture_websocket()
