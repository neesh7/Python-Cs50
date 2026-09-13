import threading
import time


def boil_mail():
    print(f"Boiling Milk....")
    time.sleep(5)
    print(f"Milk Boiled...")


def toast_bun():
    print("toasting bun...")
    time.sleep(3)
    print(f"Done with the bun toast....")



start_time = time.time()


# create threads
t1 = threading.Thread(target=boil_mail)
t2 = threading.Thread(target=toast_bun)

# now start the threads

t1.start()
t2.start()

# wait for both operations/task or threads to complete
t1.join()
t2.join()

end_time = time.time()
print(f"Breakfast is ready in {end_time - start_time: .2f} seconds")