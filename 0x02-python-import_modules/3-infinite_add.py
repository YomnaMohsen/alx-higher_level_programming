#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    t = 0
    for index in range(count):
        t += int(argv[index+1])
    print("{:d}".format(t))
