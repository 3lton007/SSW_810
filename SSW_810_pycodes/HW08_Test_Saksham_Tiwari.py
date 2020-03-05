"""
    Python program that implements test cases for functions date_arithmetic, file_reading_gen and class FileAnalyzer with functions analyze_files, pretty_print
    Author: Saksham Tiwari
"""

import unittest
from HW08_Saksham_Tiwari import date_arithmetic, file_reading_gen, FileAnalyzer

class TestModuleGeneratorFile(unittest.TestCase):
    """ Class that implements test cases for functions date_arithmetic, file_reading_gen and class FileAnalyzer with functions analyze_files, pretty_print"""
    def test_date_arithmetic(self):
        """ Checks if function date_arithmetic returns correct result """
        self.assertEqual(date_arithmetic(), ("01 Mar 2000", "02 Mar 2017", 303))

    def test_file_reading_gen(self):
        """ Checks if function file_reading_gen returns correct result """
        self.assertEqual([a for a in file_reading_gen("test.txt", 3, "|", True)], [("CWID", "Name", "Major"), ("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])
        self.assertEqual([a for a in file_reading_gen("test.txt", 3, "|", False)], [("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])

    def test_file_analyzer(self):
        """ Checks if object of class FileAnalyzer returns correct result """
        file_analyzer = FileAnalyzer("C:\\Users\\Saksham\\Desktop\\test")
        self.assertEqual({'C:\\Users\\Saksham\\Desktop\\test\\test.py': {'class': 2, 'function': 6, 'line': 19, 'char': 313}}, file_analyzer.files_summary)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)