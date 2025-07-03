# --- server/ws_sniffer.py ---
import websocket, json, threading
from hash_decoder import decode_hash
from database import save_round

def on_message(ws, message):
    data = json.loads(message)
    if 'hash' in data:
        decoded = decode_hash(data['hash'])
        save_round(data | decoded)
        print("Round saved:", data | decoded)

def run_ws():
    ws = websocket.WebSocketApp("wss://tirangagame.top/ws-endpoint", on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    threading.Thread(target=run_ws).start()
