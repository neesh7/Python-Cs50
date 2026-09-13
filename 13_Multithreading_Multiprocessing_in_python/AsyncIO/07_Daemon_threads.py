"""Daemon Threads are backgrounds threads that automatically shuts down when the main thread completes/exists
These are used in Non-critial tasks like monitoring and logging
"""

import threading
import time


def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature")
        time.sleep(2)


t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program is done")