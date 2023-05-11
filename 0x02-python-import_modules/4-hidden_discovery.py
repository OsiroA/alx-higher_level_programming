#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # open the file
    pyc = open("hidden_4.pyc", "rb")
    # read the lines of the files
    pyc_lines = pyc.readlines()
    # sort the list of lines in alphabetical order
    pyc_lines.sort()
    for line in pyc_lines:
        if not line.startswith(b"_"):
            print(line)
        #pyc_lines.startswith(b"_"):
            #continue
        #else:
            #print(pyc_lines)
    pyc.close()
