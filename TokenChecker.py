from timer import timer
from colorama import init, Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor
import requests, asyncio, aiohttp, aiofiles, os


init(convert=True)

URL = 'https://discordapp.com/api/v6/users/@me/library'

async def fetch(session, url):
    async with session.get(url) as response:
        code = response.status
        print(code)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)


def func():
    asyncio.run(main())

tokens = open("tokens.txt", 'r').read()

tokens = tokens.split('\n')

for token in tokens:
    header = {
        "Content-Type": "application/json",
        "authorization": token
    }

    code = requests.get(URL, headers=header).status_code

    if (code == 200):
        print(Back.GREEN + f"{code} - {token}\n")
        x.writelines(token + '\n')
        x.close
    elif (code == 401):
        print(Fore.RED + f"{code} - {token}\n")
        x = open('Bad.txt', 'a')
        x.writelines(token + '\n')
        x.close
    else:
        sleep(5)
        print(Fore.RED + f"{code} - Rate Limited, sleeping for 5 sec Zzz\n")