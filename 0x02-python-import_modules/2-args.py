#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments")
    else:
        if (len(sys.argv) - 1) == 1:
            print((len(sys.argv) - 1), "argument:")
            for j, arg in enumerate(sys.argv[1:], 1):
                print(f"{j}: {arg}")
        else:
            print((len(sys.argv) - 1), "arguments:")
            for j, arg in enumerate(sys.argv[1:], 1):
                print(f"{j}: {arg}")
