import threading


counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(10000):
        with lock:
            counter +=1


threads = [ threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final COunter: {counter}")

# Notes:

""" 
Without a lock, multiple threads could try to update counter simultaneously, leading to race conditions. That means:

- Two threads might read the same value of counter before either writes back.

- The final result could be less than expected, because some increments get overwritten.

"""