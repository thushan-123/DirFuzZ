import requests
import argparse
import queue

arguments = argparse.ArgumentParser(description="Dictories FuZZ tool")
arguments.add_argument("--word-list", help="Provide a WORD List text file")
arguments.add_argument("--status-codes", type=list, help="Status codes")

args = arguments.parse_args()



def fuzz():
    pass

def main():
    print("Hello from pythonfuzz!")


if __name__ == "__main__":
    main()
