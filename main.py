import asyncio
from typing import List
import aiohttp
import requests
import argparse
import queue
from url_builder import UrlBuilder
from file_builder import FileUrlBuilder
from requests.exceptions import RequestException
from urllib.parse import urlparse

arguments = argparse.ArgumentParser(description="Dictories FuZZ tool")
arguments.add_argument("--word-list", help="Path Word List text file", required=True)
arguments.add_argument("--status-codes", type=str, help="Status codes", default="200,301,302,403")
arguments.add_argument("-e", type=str , help="file extensions")
arguments.add_argument("-fname" , help="file nale lis not provided default list is word list")
arguments.add_argument("-r" , help="recursive fuzz <number> 0-5")
arguments.add_argument("--url", type=str, help="Target URL", required=True)

args = arguments.parse_args()

Q = queue.Queue()
file_queue = queue.Queue()
# nargs='+' indicates one or more arguments 
# nargs='*' indicates zero or more arguments 

code = args.status_codes
#extensions_arr = (args.e).split(",")
status_code_str_arr:list = code.split(",")
status_codes = [int(x) for x in status_code_str_arr]

file_extenctions_str = args.e 
file_extenctions = file_extenctions_str.split(",")


try:
    with open(args.word_list, 'r') as f:
        data = f.read()
        print(data.encode())
        word_l = data.split("\n")
        for x in word_l:
            Q.put(x)      
except FileNotFoundError:
    print(f"File is Not Found : {args.word_list}")
    exit(1)
    
    
if args.fname:
    with open(args.fname, 'r') as f:
        for fname in f.read().splitlines():
            file_queue.put(fname)
else:
    file_queue = Q

async def check_url(session: aiohttp.ClientSession, url: str):
    try:
        async with session.get(url) as response:
            if response.status in status_codes:
                print(f"{url}  status:{response.status}")
                return True
    except Exception as e:
        print(f"Error: {url} -> {e}")
    return False

async def check_and_recurse(session: aiohttp.ClientSession, url: str, word: str, depth: int, max_depth: int):
    is_valid = await check_url(session, url)
    if is_valid and depth < max_depth:
        # Recursive fuzzing
        with open(args.word_list, 'r') as f:
            sub_words = f.read().splitlines()
            await fuzz(session, url + "/", sub_words, depth + 1, max_depth)


async def fuzz(session: aiohttp.ClientSession, base_url: str, words: List[str], depth: int = 0, max_depth: int = 0):
    if depth > max_depth:
        return

    url_builder = UrlBuilder(base_url)
    tasks = []

    for word in words:
        url = url_builder.add_dir(word)
        task = asyncio.create_task(check_and_recurse(session, url, word, depth, max_depth))
        tasks.append(task)

    await asyncio.gather(*tasks)

def file_fuzz():
    global file_queue
    file_n = None
    if args.fname is None:
        file_queue = Q
    else:
        with open(args.fname, 'r') as l:
            n = l.read()
            k = n.split("\n")
            
            for x in k:
                file_queue.put(x)

    while not file_queue.empty():
        name = file_queue.get()
        for x in file_extenctions:
            file_bulder = FileUrlBuilder(args.url,x)
            y =file_bulder.fileUrlPathBuilder(name)
            r = requests.get(url=y)
            if r.status_code in status_codes:
                print(y)    
        

def main():
    print("\nHello from pythonfuzz!")
    print("___________________________")
    print("")
    
    print(f"WORD LIST     : {args.word_list}")
    print(f"STATUS CODES  : {args.status_codes}")
    print("___________________________")
    
    print("")
    fuzz()
    file_fuzz()
    


if __name__ == "__main__":
    main()
    
