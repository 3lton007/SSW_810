"""

@eltonaloys 

"""

import unittest
from HW09_Elton_Aloys import Student, Instructor, Repository

class StudentTest(unittest.TestCase):
    """ Class to check class Student """
    def test_student(self):
        """ Function that tests class Student """
        student = Student("Elton ALoysius", "Software Engineering")
        self.assertEqual(student.student_name, "Elton Aloysius")  
        self.assertEqual(student.student_major, "Software Engineering")  
        
class InstructorTest(unittest.TestCase):
    """ Class to check class Instructor """
    def test_instructor(self):
        """ Function that tests class Instructor """
        instructor = Instructor("James Rowland", "Software Engineering")
        self.assertEqual(instructor.instructor_name, "James Rowland")  
        self.assertEqual(instructor.instructor_dept, "Software Engineering") 
        
class RepositoryTest(unittest.TestCase):
    """ Class to tests class Repository """
    def test_repository(self):
        """ Function that tests class Repository """
        repository = Repository("D:\PythonDev\.vscode")

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)