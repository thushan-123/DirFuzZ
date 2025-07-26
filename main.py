import requests
import argparse
import queue

arguments = argparse.ArgumentParser(description="Dictories FuZZ tool")
arguments.add_argument("--word-list", help="Path Word List text file", required=True)
arguments.add_argument("--status-codes", type=str, help="Status codes", default="200,301,302,403")

args = arguments.parse_args()

Q = queue.Queue()

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
    while not Q.empty():
        word: str = Q.get()
        print(word)

def main():
    print("\nHello from pythonfuzz!")
    print("___________________________")
    print("")
    
    print(f"WORD LIST     : {args.word_list}")
    print(f"STATUS CODES  : {args.status_codes}")
    print("___________________________")
    
    print("")
    fuzz()
    


if __name__ == "__main__":
    main()
    
