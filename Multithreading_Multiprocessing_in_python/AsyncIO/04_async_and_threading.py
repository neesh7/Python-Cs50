import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# This is a normal function
def check_stock(item):
    print(f"checking {item} in store...")
    time.sleep(3)
    return f"{item} Stock 42"

# coroutine
async def main():
    # if your app already using threading then using this loop we can increase the efficiency
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        # run in executor lets you run async function into a separate thread
        result = await loop.run_in_executor(pool, check_stock,"Masala chai")
        print(result)

asyncio.run(main())