import asyncio


# Co-routine function
async def brew_chai():
    print("Brew Chai...")
    await asyncio.sleep(2)
    print("Chai is Ready...")



asyncio.run(brew_chai())