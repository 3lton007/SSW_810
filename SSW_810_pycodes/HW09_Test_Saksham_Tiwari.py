"""
    Python program that tests classes Student, Instructor, Repository
    Author: Saksham Tiwari
    Date: 10/30/2019 12:18
"""

import unittest
from HW10_Elton_Aloys import Student, Instructor, Repository

class StudentTest(unittest.TestCase):
    """ Class that tests class Student """
    def test_student(self):
        """ Function that tests class Student """
        student = Student("Saksham Tiwari", "Software Engineering")
        self.assertEqual(student.student_name, "Saksham Tiwari")  
        self.assertEqual(student.student_major, "Software Engineering")  
        
class InstructorTest(unittest.TestCase):
    """ Class that tests class Instructor """
    def test_instructor(self):
        """ Function that tests class Instructor """
        instructor = Instructor("James Rowland", "Software Engineering")
        self.assertEqual(instructor.instructor_name, "James Rowland")  
        self.assertEqual(instructor.instructor_dept, "Software Engineering")  
        
class RepositoryTest(unittest.TestCase):
    """ Class that tests class Repository """
    def test_repository(self):
        """ Function that tests class Repository """
        repository = Repository("D:\PythonDev\.vscode")

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)