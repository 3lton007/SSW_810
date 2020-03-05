"""

TestCases for ReverseString , ReverseEnumerate , SecondOccurance
@eltonaloys

"""
def reverse(str):
    """ To reverse a string"""
    try:
        return str[::-1]

        
    except TypeError:
        print("Enter a Valid String:")
        return -1


def rev_enumerate(s):
    """To Reverse Enumerate"""
    try:
        for i in range((len(s) - 1),-1, -1):
            yield i, s[i]
    except TypeError:
        return -1   

def find_second(target, str):
    """ To find the Second occurance in the string"""
    try:
        index = str.find(target)
        str = str[index + len(target) : len(str)]
        index = str.find(target) + index + len(target)
        return index
    except TypeError:
        print("Enter a Valid String")
        return -1


def get_lines(path):
    """ To remove Comments and Combine the File  """
    try:
        tp = open(path, "r")
    except FileNotFoundError:
        print(f"Can't open {path}")
    else:
        with tp:
            n_line = ""
            for line in tp:
                line = line.strip()

                if line[len(line) - 1] == "\\":
                    n_line = n_line + line[: len(line) - 1]
                    continue

                if len(n_line) != 0:
                    if n_line[0] == "#":
                        continue
                    elif n_line.find("#") == -1:
                        yield n_line + line
                        n_line = ""
                    else:
                        n_line = n_line + line
                        n_line = n_line[: n_line.find("#")]
                        yield n_line
                        n_line = ""
                else:
                    if line[0] == "#":
                        continue
                    elif line.find("#") == -1:
                        yield line
                    else:
                        line = line[: line.find("#")]
                        yield line                



get_lines("elton99.txt")