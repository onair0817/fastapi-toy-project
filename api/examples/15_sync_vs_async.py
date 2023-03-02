import asyncio
import time


def sync_gen_int_and_print(name: str, a: int, sleep: int = 1):
    for i in range(a):
        print(name, " ::: ", i)
        time.sleep(sleep)


def sync_main(names):
    for name, a in names:
        sync_gen_int_and_print(name, a)


async def gen_int_and_print(name: str, a: int, sleep: int = 1):
    for i in range(a):
        print(name, " ::: ", i)
        await asyncio.sleep(sleep)


async def async_main(names):
    async_gens = [gen_int_and_print(name, a) for name, a in names]
    await asyncio.gather(*async_gens)


if __name__ == "__main__":
    names = [(chr(name), 3) for name in range(65, 91)]

    tic = time.time()
    sync_main(names)
    toc = time.time()
    print(toc - tic)

    print()

    tic = time.time()
    asyncio.run(async_main(names))
    toc = time.time()
    print(toc - tic)
