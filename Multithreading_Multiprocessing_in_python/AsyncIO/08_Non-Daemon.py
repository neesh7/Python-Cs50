"""Non-Daemon Threads are backgrounds threads that keeps continuosly running even"""

import threading
import time


def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature")
        time.sleep(2)


# t = threading.Thread(target=monitor_tea_temp, daemon=True) # Daemon Threads
t = threading.Thread(target=monitor_tea_temp) # Non-Daemon Threads
t.start()

print("Main program is done")