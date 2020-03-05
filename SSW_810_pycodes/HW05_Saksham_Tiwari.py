def reverse(string):
    """ Function that takes string as an argument and reverses it """
    reversed_string = ""

    try:
        for i in range((len(string) - 1), -1, -1):
            reversed_string = reversed_string + string[i]
    except TypeError:
        print("Enter a valid string")
        return -1

    return reversed_string

def rev_enumerate(list):
    """ Function that works just like enumerate, but in a reversed order"""
    try:
        for i in range(len(list) - 1, -1, -1):
            yield i, list[i]
    except TypeError:
        print("Enter a valid list")
        return -1 

def find_second(target, string):
    """Function that returns the index of second occurrence of the target string in a string """
    index = string.find(target)
    if index == -1:
        return -1
    string = string[index + len(target): len(string)]
    index = string.find(target) + index + len(target)
    return index

def get_lines(path):
    """  """
    file_name = path
    try:
        fp = open(file_name, "r")
    except FileNotFoundError:
        print(f"Can't open {file_name}")
    else:
        with fp:
            for line in fp:
                line = line.strip()
                

                if line.find("#") == -1:
                    if line[len(line) - 1] == "\\":
                        print(line[0: len(line) - 1], end = "")
                    else:
                        print(line)
                elif line[0] == "#":
                    pass    
                else:
                    line = line[: line.find("#")]
                    if line[len(line) - 1] == "\\":
                        print(line[0: len(line) - 1], end = "")
                    else:
                        print(line)

get_lines("name.txt")