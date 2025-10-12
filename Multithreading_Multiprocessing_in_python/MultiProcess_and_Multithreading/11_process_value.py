from multiprocessing import Process, Queue, Value


def increment(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value +=1






if __name__=="__main__":
    counter = Value('i', 0)
    
   # our set of intended task is stored inside the queue and process will pick them from queue and will do it one after another
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes ] 
    [p.join() for p in processes ] 
    
    print("Final counter vlaue:",counter.value)