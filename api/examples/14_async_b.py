import asyncio


async def gen_int_and_print(name: str, a: int, sleep: int = 1):
    for i in range(a):
        print(name, " ::: ", i)
        await asyncio.sleep(sleep)


async def main(gens):
    await asyncio.gather(*gens)


if __name__ == "__main__":
    names = [("i", 2), ("j", 5), ("k", 8)]
    gens = [gen_int_and_print(name, a) for name, a in names]
    # print(gens[0])
    asyncio.run(main(gens))
