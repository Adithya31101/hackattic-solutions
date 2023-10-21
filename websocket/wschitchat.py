from requests import get, post
import websocket
from datetime import datetime
import math

res = get("https://hackattic.com/challenges/websocket_chit_chat/problem?access_token=b53b9d130f72e759")
val = res.json()
token = val['token']
getmillis = lambda: int((datetime.now() - start).total_seconds() * 1000)
start = None

def get_approx(val, opts):
    min_diff = math.inf
    index = 0
    for i in range(len(opts)):
        diff = abs(val - opts[i])
        if diff < min_diff:
            min_diff = diff
            index = i
    print(f"Predicted opt {opts[index]} for elapsed time {val}")
    return opts[index]


def on_message(ws, message):
    global start
    if message == 'ping!':
      delta = getmillis()
      start = datetime.now()
      elapsed = get_approx(delta, [700, 1500, 2000, 2500, 3000])
      ws.send(str(elapsed))
      print("sent", elapsed, "back to the server!")
    else:
        print(message)
def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    global start
    start = datetime.now()
    print("Opened connection")

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://hackattic.com/_/ws/{token}",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.run_forever()