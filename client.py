import aiohttp
import asyncio
import json


async def call_api_server(session):
    async with session.get("http://localhost:8000/api") as resp:
        return await resp.json()


async def main():
    async with aiohttp.ClientSession() as session:
        result = await call_api_server(session)
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    asyncio.run(main())
