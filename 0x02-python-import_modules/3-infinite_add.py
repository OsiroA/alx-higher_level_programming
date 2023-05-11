#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from add_0 import add
    # get the length of the arguments passed on the command line
    c = sys.argv
    x = len(c) - 1
    a, b = 0, int(sys.argv[1])
    for i in range(2, (x + 1)):
        a, b = b, b + int(sys.argv[i])
        # i += 1
        if i == x:
            a = a + int(sys.argv[i])
    print(a)
