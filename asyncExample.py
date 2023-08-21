import aiohttp
import asyncio

url = "https://aoe2.net/api/strings?game=aoe4&language=en"

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        print("Before ..")
        html = await fetch(session, url)
        print("After ...", html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())