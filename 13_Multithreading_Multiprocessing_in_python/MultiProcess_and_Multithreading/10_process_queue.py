from multiprocessing import Process, Queue
import time


def prepare_chai(queue):
    queue.put("Masala Chai is ready")





if __name__=="__main__":

    # Queue inititallization
    queue = Queue()

    # our set of intended task is stored inside the queue and process will pick them from queue and will do it one after another
    p = Process(target=prepare_chai, args=(queue, ))
    p.start()
    p.join()
    print(queue.get())