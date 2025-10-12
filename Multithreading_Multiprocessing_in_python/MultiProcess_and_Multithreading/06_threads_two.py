import threading
import time


def prepare_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai ready...")




start_time = time.time()


# create threads
t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Adrak", 4))

# now start the threads

t1.start()
t2.start()

# wait for both operations/task or threads to complete
t1.join()
t2.join()

end_time = time.time()
print(f"Chai is ready in {end_time - start_time: .2f} seconds")