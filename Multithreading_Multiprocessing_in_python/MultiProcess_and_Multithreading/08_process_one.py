import threading
import time


def cpu_heavy():
    print(f'crunchcing some numbers...')
    total = 0 
    for i in range(10**8):
        total +=1

    print("Done ")

start = time.time()
ths = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in ths]
[t.join() for t in ths]

print(f"Time taken: {time.time() - start:.2f} seconds")