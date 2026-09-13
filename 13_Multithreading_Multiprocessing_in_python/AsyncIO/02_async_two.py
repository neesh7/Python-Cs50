import asyncio
import time


async def brew_chai(chai):
    print(f"Brewing {chai} ...")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f"{chai} is Ready...")

async def brew_coffee(coffee):
    print(f"Brewing {coffee} ...")
    await asyncio.sleep(2)
    print(f"{coffee} is Ready...")

async def main():
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Adrak"),
        brew_chai("Elaichi"),
        brew_coffee("Capachino"),
        brew_coffee("Black Coffee"),
    )

asyncio.run(main())