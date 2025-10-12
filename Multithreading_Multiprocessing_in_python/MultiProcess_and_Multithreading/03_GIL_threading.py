import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(1000):
        count +=1
        print(f"{threading.current_thread().name} finished brewing...")



# create thread
thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
# start the thread
thread1.start()
thread2.start()


# wait for both operations/task or threads to complete
thread1.join()
thread2.join()

end = time.time()

print("All Orders taken and chai brewed !")
print(f"Total time taken {end - start}")