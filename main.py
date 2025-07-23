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
        word_l = data.split("\n")
        for x in word_l:
            Q.put(x)      
except :
    raise Exception()



def fuzz():
    pass

def main():
    print("\nHello from pythonfuzz!")
    print("___________________________")
    print("")
    
    print(f"WORD LIST     : {args.word_list}")
    print(f"STATUS CODES  : {args.status_codes}")
    print("___________________________")


if __name__ == "__main__":
    main()
