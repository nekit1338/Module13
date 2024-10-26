import asyncio


async def start_strongman(name: str, power: int):
    print("Силач {} начал соревнования.".format(name))
    for i in range(1, 6):
        await asyncio.sleep(5 / power)
        print('Силач {} поднял {} шар'.format(name, i))
    print("Силач {} закончил соревнования.".format(name))


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(start_tournament())
