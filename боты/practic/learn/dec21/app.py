import asyncio
from contextvars import ContextVar
Mycounter = ContextVar('counter', default= 0)
async def increase():
    my_counter = Mycounter.get()
    my_counter += 1
    Mycounter.set(my_counter)

async def count():
    while True:
        await increase()
        my_counter = Mycounter.get()
        print(f'counter: {my_counter}')
        await asyncio.sleep(1)
asyncio.run(count())