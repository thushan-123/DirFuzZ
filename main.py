from typing import List
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
recursive_queue = queue.Queue()
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



def fuzz():
    url_builder = UrlBuilder(args.url)
    while not Q.empty():
        word: str = Q.get()
        url_ = url_builder.add_dir(word)
        # print(urlparse(url_))
        try:
            r = requests.get(url=url_)
            
            if r.status_code in status_codes:
                print(f"{url_}  status:{r.status_code}")
                if args.r is not None:
                    recursive_queue.put(word)
        except RequestException as e:
            print(e)
            break

def file_fuzz():
    file_n = None
    if args.fname is None:
        file_n = args.word_list
    else:
        file_n = args.fname
    for x in file_extenctions:
        file_bulder = FileUrlBuilder(args.url,args.word_list,x)
        y =file_bulder.fileUrlPathBuilder(x)
        print(y)
        
def recursive_fuzz():
    if args.r < 6:
        pass
    else:
        print("value is out of scope")
    
            
            
        
        

def main():
    print("\nHello from pythonfuzz!")
    print("___________________________")
    print("")
    
    print(f"WORD LIST     : {args.word_list}")
    print(f"STATUS CODES  : {args.status_codes}")
    print("___________________________")
    
    print("")
    #fuzz()
    file_fuzz()
    


if __name__ == "__main__":
    main()
    
