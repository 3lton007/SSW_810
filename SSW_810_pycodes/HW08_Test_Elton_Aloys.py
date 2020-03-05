import unittest
"""

@eltonaloys

"""


from HW08_Elton_Aloys import date_arithmetic, file_reading_gen, FileAnalyzer

class TestModuleGeneratorFile(unittest.TestCase):
    """ To check for ModuleGeneratorFile """

    def test_date_arithmetic(self):
        """ check for date arithmetic """
        self.assertTrue(date_arithmetic() == ('01 Mar 2000', '02 Mar 2017', 303))

    
    def test_file_reading_gen(self):
        """ TO check for file reading with header and seperated by | """
        self.assertEqual([a for a in file_reading_gen("D:\PythonDev\.vscode\eltonio.txt", 3, "|", True)], [("CWID", "Name", "Major"), ("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])
        self.assertEqual([a for a in file_reading_gen("D:\PythonDev\.vscode\eltonio.txt", 3, "|", False)], [("123", "Jin He", "Computer Science"), ("234", "Nanda Koka", "Software Engineering"), ("345", "Benji Cai", "Software Engineering")])


    def test_file_analyzer(self):
        """ Checks if object of class FileAnalyzer returns correct result """
        file_analyzer = FileAnalyzer("D:\\PythonDev\\.vscode\\test")
        self.assertEqual({'D:\\PythonDev\\.vscode\\test\\test.py': {'class': 0, 'function': 6, 'line': 14, 'char': 219}}, file_analyzer.files_summary)

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)  

