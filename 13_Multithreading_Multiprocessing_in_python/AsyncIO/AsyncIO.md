# Async Python


We can achieve similar speed as Multiprocessing or MultiThreading by using Async (Synchronous programming). We don't need to fall to Advance methods.

For instance, if we want to do these :

- fetch 10 web pages
- Read 20 files
- Send 100 HTTP requests

Using Async we do multiple operations concurrently without actually waiting for the results of running tasks.

- `async def`, declares a coroutine (Special function that can be paused)
- `await` (In order to use await the function needs to be async), pauses the execution untill the result is ready
- `asyncio`, Built-in Python Library
- `Event Loop`, The engine that runs and schedule co-routines in python

#### Blocking vs Non-Blocking operations
- time.sleep(2) : it's a blocking operations as it waits for 2 sec
- await asyncio.sleep(2): This is non-blocking as it can parallely handle multiple calls

## Daemon and Non-Daemon

#### 👻 Daemon Threads
- These are background threads.

- Python does NOT wait for them(main) to finish.

- They’re killed abruptly when the main thread exits.

- Use them for tasks like monitoring, heartbeat pings, or cleanup routines that shouldn’t block shutdown.
```python
t = threading.Thread(target=task)
t.daemon = True
t.start()
# Main thread can exit even if `t` is still running
```
#### 🧵 Non-Daemon Threads (Default)
- These are normal threads.

- The Python program waits for them to finish before exiting.

- Example: If you spawn a thread to process logs, the main script won’t exit until that thread completes.

```
python
t = threading.Thread(target=task)
t.start()
# Main thread waits for `t` to finish before exiting
```

| Feature              | Non-Daemon Thread       | Daemon Thread            |
|----------------------|-------------------------|--------------------------|
| Blocks program exit  | ✅ Yes                  | ❌ No                    |
| Use for critical work| ✅ Yes                  | ❌ No                    |
| Use for background   | ❌ Not ideal            | ✅ Yes                   |
| Graceful shutdown    | ✅ Yes                  | ❌ No (may be killed)    |


## Profiling
it tells the amount of time spend in each functions.


python -m cProfile -s time <codename.py>

- These tools are used to check for profiling or debugging or checking for deadlock or race condition: **pyspy, vprof**

## Race Condition vs Deadlock

## 🧵 Threading Concepts: Deadlock vs Race Condition

### 🔒 Deadlock

- **Definition**: A situation where two or more threads are waiting indefinitely for resources locked by each other.
- **In Our Context**: If you had multiple locks (e.g., `lock1`, `lock2`) and threads acquired them in different orders, they could block each other forever.

#### Example Scenario:
```python
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_a():
    with lock1:
        time.sleep(1)
        with lock2:
            pass

def thread_b():
    with lock2:
        time.sleep(1)
        with lock1:
            pass
```

- thread_a holds lock1 and waits for lock2

- thread_b holds lock2 and waits for lock1

- Both threads are stuck → deadlock


## Race Condition
- Definition: A flaw that occurs when multiple threads access and modify shared data concurrently, and the outcome depends on the timing of their execution.

- In Our Context: If you remove the with lock: from your increment() function, multiple threads could update counter at the same time, leading to incorrect results.

- Example Scenario:
```python
def increment():
    global counter
    for _ in range(10000):
        counter += 1  # No lock!
```
- Threads might read the same value of counter before writing back.

- Final value could be less than expected → race condition
#### Summary table
| Concept         | Description                                                  | In Your Code Example                          |
|-----------------|--------------------------------------------------------------|------------------------------------------------|
| Deadlock        | Threads wait forever due to circular lock dependencies       | Happens with multiple locks and bad ordering   |
| Race Condition  | Threads overwrite each other's changes unpredictably         | Happens if `lock` is removed from `increment()`|
