from multiprocessing import Process
import time

# This is actually multicore work - where we have multiple cores to handle multiple task so basically multiprocessing

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")


if __name__=="__main__":
    chai_makers = [ Process(target=brew_chai, args=(f"Chai Maker #{i+1}",)) for i in range(3)]

    # start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All Chai Served")