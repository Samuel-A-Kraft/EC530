import threading
import time
from app.sockets import launch_listener, deliver_message

def run_cli():
    while True:
        try:
            ip = input("Send to IP (or 'exit'): ").strip()
            if ip == "exit":
                break
            port = int(input("Port: ").strip())
            msg = input("Message: ").strip()
            deliver_message(ip, port, msg)
        except Exception as err:
            print(f"[Error] {err}")

if __name__ == "__main__":
    print("Launching peer node...")
    listener = threading.Thread(target=launch_listener, args=(9000,), daemon=True)
    listener.start()
    time.sleep(0.5)
    run_cli()
