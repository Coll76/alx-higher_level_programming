#!/usr/bin/python3
for loer_case in range(ord('a'), ord('z') + 1):
    if (loer_case == ord('q') or loer_case == ord('e')):
        continue
    print("{}".format(chr(loer_case)), end='')
