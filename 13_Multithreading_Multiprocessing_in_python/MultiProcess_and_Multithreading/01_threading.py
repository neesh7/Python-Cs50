import threading
import time

# This is basically an example for concurrency
# This is using 1 core in actual.
# A single guy switching between different task
def take_orders():
    for i in range(1,4):
        print(f"Taking order #{i}")
        time.sleep(2)


def brewing_chai():
    for i in range(1,4):
        print(f"Brewing chai #{i}")
        time.sleep(5)


# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brewing_chai)

# now start the threads

order_thread.start()
brew_thread.start()

# wait for both operations/task or threads to complete
order_thread.join()
brew_thread.join()

print("All Orders taken and chai brewed !")