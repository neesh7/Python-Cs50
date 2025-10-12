from multiprocessing import Process
import time


def cpu_heavy():
    print(f'crunchcing some numbers...')
    total = 0 
    for i in range(10**9):
        total +=1

    print("Done ")


if __name__=="__main__":
    start = time.time()
    processess = [Process(target=cpu_heavy) for _ in range(2)]
    [process.start() for process in processess]
    [process.join() for process in processess]

    print(f"Time taken: {time.time() - start:.2f} seconds")