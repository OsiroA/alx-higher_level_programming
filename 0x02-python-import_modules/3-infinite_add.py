#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from add_0 import add
    # get the length of the arguments passed on the command line
    c = sys.argv
    x = len(c) - 1
    a, b = 0, 0
    #a, b = 0, int(sys.argv[1])
    for i in range(1, (x + 1)):
        try:
            b = int(sys.argv[i])
            a += b
        except:
        # i += 1
        #if i == x:
            print("Invalid argumment: {}".format(sys.argv[i]))
            sys.exit(1)
    print(a)
