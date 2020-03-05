"""

Implementing functions date_arithmetic, file_reading_gen and class FileAnalyzer
@eltonaloys

"""

import os
from datetime import datetime, timedelta
from prettytable import PrettyTable

def date_arithmetic():
    """ Arithmetic operations on dates"""
    date_first = datetime.strptime("27 Feb 2000", "%d %b %Y")
    date_second = datetime.strptime("27 Feb 2017", "%d %b %Y")
    date_diff = datetime.strptime("31 Oct 2017", "%d %b %Y") - datetime.strptime("1 Jan 2017", "%d %b %Y")
    

    return ((date_first + timedelta(days = 3)).strftime("%d %b %Y"), (date_second + timedelta(days = 3)).strftime("%d %b %Y"), date_diff.days)
                

def file_reading_gen(path, fields, sep=',', header = False):
    """ Generator to read fields in  a file """
    try:
        fp = open(path,"r")
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        with fp:
            if header is False:
                next(fp)
                
            for offset, line in enumerate(fp):
                current = line.strip().split(sep)
                if len(current) != fields:
                    raise ValueError(f" {fp} has {len(current)} on line {offset} and {fields} ")
                else:
                    yield tuple(line.strip().split(sep))


class FileAnalyzer:
    """ Class to implement analyze_filers, pretty_print """

    def __init__(self, dir):
        """ Function to initalizes variable directory and opens the directory """
        self.dir = dir
        try:
            self.list_of_python_files = [file for file in os.listdir(dir) if file.endswith(".py")]
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            self.analyze_files()

    def analyze_files(self):
        """ Function to count number of lines, characters, functions and classes in a file """
        self.files_summary = {}
        for file in self.list_of_python_files:
            file_name = os.path.join(self.dir, file)
            num_lines, num_char, num_func, num_class = 0, 0, 0, 0

            with open(file_name, "r") as fp:
                for line in fp:
                    line = line.strip()
                    num_lines += 1
                    num_char = num_char + len(line)
                    if line.startswith("def ") and line.endswith(":"):
                        num_func += 1
                    elif line.startswith("class ") and line.endswith(":"):
                        num_func += 1
                        self.files_summary[file_name] = {"class": num_class, "function": num_func, "line": num_lines, "char": num_char}
                        
    def pretty_print(self):
        """ To print the file summary in a table"""
        pretty_table = PrettyTable(field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.files_summary:
            pretty_table.add_row ([file_name, self.files_summary[file_name]["class"], self.files_summary[file_name]["function"], self.files_summary[file_name]["line"], self.files_summary[file_name]["char"]])

        return pretty_table


object = FileAnalyzer('D:\PythonDev\.vscode').pretty_print()
print(object)










