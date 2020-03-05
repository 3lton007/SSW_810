

def reverse(s):
    """To reverse a given string """
    string = ''
    for i in range((len(s) -1), -1, -1):
        string += s[i]
    return string
        
#string = str(input('enter the string'))
print(reverse("string"))

def rev_enumerate(seq):
    """ To enumerate and print in reverse"""
    for i in range((len(seq) -1), -1, -1):
        yield i, seq[i]
#s = 'hello world'
    
#for index,value in rev_enumerate(s):
#    print(index, value)

def find_second(target, string):
    """ To find the second occurrence """
    i = string.find(target)
    string = string[i + len(target) : len(string)]
    i += string.find(target) + len(target)
    return i
#st = 'mississippi'
#print(find_second('iss', st))

def get_lines(path):
    """ Function that returns each line in a file, one by one when called """
    try:
        tp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find file")
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