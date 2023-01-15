import asyncio
import time

import aiohttp
start_time = time.time()


async def fun1():
    print('fun1 starting...')

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('http://fakedomain') as response:

                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:15], "...")
                print('fun1 завершена')
        except Exception as error:
            print(f"The error '{error}' occurred")
            print('fun1 завершена')

async def fun2():
    print('fun2 starting...')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())

    await task1
    await task2




#print(time.strftime('%X'))

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
#print(time.strftime('%X'))