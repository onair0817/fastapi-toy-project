import asyncio
import aiohttp


async def send_request_periodically():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://localhost:8000/ingress",
                json={"url": "some-url", "params": {"key": "value"}},
            ) as resp:
                response = await resp.json()
                print(response)
        await asyncio.sleep(10)


async def main():
    await asyncio.gather(
        send_request_periodically(),
    )


if __name__ == "__main__":
    asyncio.run(main())


""" 
import asyncio
import aiohttp

async def call_api_server(session, url):
    async with session.get(url) as resp:
        response = await resp.json()
        # Check if a specific condition is met in the response
        if 'condition' in response:
            # Make another API call with the new data obtained from the response
            new_url = response['new_data']
            await call_api_server(session, new_url)
        return response

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = ['http://api_server_1.com', 'http://api_server_2.com', 'http://api_server_3.com']
        tasks = [asyncio.ensure_future(call_api_server(session, url)) for url in url_list]
        responses = await asyncio.gather(*tasks)
        print(responses)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""
