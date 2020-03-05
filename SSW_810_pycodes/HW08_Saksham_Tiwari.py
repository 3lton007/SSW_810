"""
    Python program that implements fucntions date_arithmetic, file_reading_gen and class FileAnalyzer with functions analyze_files, pretty_print
    Author: Saksham Tiwari
"""

import os
from datetime import datetime, timedelta
from prettytable import PrettyTable

def date_arithmetic():
    """ Function that performs arithmetic operation on dates """
    date_one = datetime.strptime("27 Feb 2000", "%d %b %Y")
    date_two = datetime.strptime("27 Feb 2017", "%d %b %Y")
    date_three = datetime.strptime("31 Oct 2017", "%d %b %Y") - datetime.strptime("1 Jan 2017", "%d %b %Y")

    return ((date_one + timedelta(days=3)).strftime("%d %b %Y"), (date_two + timedelta(days=3)).strftime("%d %b %Y"), date_three.days)

def file_reading_gen(path, fields, sep=",", header=False):
    """ Generator that reads all the fields in a file """
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find/open file at location {path}")
    else:
        with fp:
            for offset, line in enumerate(fp, start=1):
                if header == False:
                    header = True
                    continue
                elif line.find(sep) == -1:
                    continue

                if len(line.strip().split(sep)) != fields:
                    raise ValueError()
                else:
                    yield tuple(line.strip().split(sep))

class FileAnalyzer:
    """ Class that implements functions analyze_files, pretty_print """
    def __init__(self, directory):
        """ Function that initializes variable directory and opens the directory """
        self.directory = directory
        try:
            self.list_of_python_files = [file for file in os.listdir(directory) if file.endswith(".py")]
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find/open file at location {directory}")
        else:
            self.analyze_files()

    def analyze_files(self):
        """ Function that counts  number of lines, characters, function and classes in a file"""
        self.files_summary = {}
        for file in self.list_of_python_files:
            file_name = os.path.join(self.directory, file)
            number_of_lines, number_of_characters, number_of_functions, number_of_classes = 0, 0, 0, 0            
            
            with open(file_name, "r") as fp:
                for line in fp:
                    line = line.strip()
                    number_of_lines += 1
                    number_of_characters = number_of_characters + len(line)
                    if line.startswith("def ") and line.endswith(":"):
                        number_of_functions += 1
                    elif line.startswith("class ") and line.endswith(":"):
                        number_of_classes += 1

            self.files_summary[file_name] = {"class": number_of_classes, "function": number_of_functions, "line": number_of_lines, "char": number_of_characters}

    def pretty_print(self):
        """ Funtion that prints files_summary in tabular form """
        pretty_table = PrettyTable(field_names=["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.files_summary:
            pretty_table.add_row([file_name, self.files_summary[file_name]["class"], self.files_summary[file_name]["function"], self.files_summary[file_name]["line"], self.files_summary[file_name]["char"]])
        
        return pretty_table