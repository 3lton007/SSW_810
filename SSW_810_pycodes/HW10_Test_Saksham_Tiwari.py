"""
    Python program that tests classes Student, Instructor, Repository
    Author: Saksham Tiwari
    Date: 10/30/2019 12:18
"""

import unittest
from HW10_Saksham_Tiwari import Student, Instructor, Repository

class StudentTest(unittest.TestCase):
    """ Class that tests class Student """
    def test_student(self):
        """ Function that tests class Student """
        student = Student("Saksham Tiwari", "Software Engineering")
        self.assertEqual(student.student_name, "Saksham Tiwari")  
        self.assertEqual(student.student_major, "Software Engineering") 
        self.assertEqual(student.student_completed_courses, []) 
        self.assertEqual(student.student_remaining_required_courses, []) 
        self.assertEqual(student.student_remaining_elective_courses, []) 
        
class InstructorTest(unittest.TestCase):
    """ Class that tests class Instructor """
    def test_instructor(self):
        """ Function that tests class Instructor """
        instructor = Instructor("James Rowland", "Software Engineering")
        self.assertEqual(instructor.instructor_name, "James Rowland")  
        self.assertEqual(instructor.instructor_dept, "Software Engineering") 
        self.assertEqual(instructor.instructor_courses_with_students, {})  
        
class RepositoryTest(unittest.TestCase):
    """ Class that tests class Repository """
    def test_repository(self):
        """ Function that tests class Repository """
        repository = Repository("C:\\Users\\Saksham\\Desktop\\810\\SSW-810")
        expected = {'SFEN': {'R': ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], 'E': ['CS 501', 'CS 513', 'CS 545']}, 'SYEN': {'R': ['SYS 612', 'SYS 671', 'SYS 800'], 'E': ['SSW 540', 'SSW 565', 'SSW 810']}}
        output = repository.majors_summary
        self.assertEqual(expected, output)

        expected = ["Name: Baldwin, C, Major: SFEN, Completed courses: ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], Remaining required courses: ['SSW 540', 'SSW 555'], Remaining elective courses: None", "Name: Wyatt, X, Major: SFEN, Completed courses: ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], Remaining required courses: ['SSW 540', 'SSW 555'], Remaining elective courses: None", "Name: Forbes, I, Major: SFEN, Completed courses: ['SSW 555', 'SSW 567'], Remaining required courses: ['SSW 540', 'SSW 564'], Remaining elective courses: ['CS 501', 'CS 513', 'CS 545']", "Name: Erickson, D, Major: SFEN, Completed courses: ['SSW 564', 'SSW 567', 'SSW 687'], Remaining required courses: ['SSW 540', 'SSW 555'], Remaining elective courses: ['CS 501', 'CS 513', 'CS 545']", "Name: Chapman, O, Major: SFEN, Completed courses: ['SSW 689'], Remaining required courses: ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], Remaining elective courses: ['CS 501', 'CS 513', 'CS 545']", "Name: Cordova, I, Major: SYEN, Completed courses: ['SSW 540'], Remaining required courses: ['SYS 612', 'SYS 671', 'SYS 800'], Remaining elective courses: None", "Name: Wright, U, Major: SYEN, Completed courses: ['SYS 611', 'SYS 750', 'SYS 800'], Remaining required courses: ['SYS 612', 'SYS 671'], Remaining elective courses: ['SSW 540', 'SSW 565', 'SSW 810']", "Name: Kelly, P, Major: SYEN, Completed courses: [], Remaining required courses: ['SYS 612', 'SYS 671', 'SYS 800'], Remaining elective courses: ['SSW 540', 'SSW 565', 'SSW 810']", "Name: Morton, A, Major: SYEN, Completed courses: ['SYS 611', 'SYS 645'], Remaining required courses: ['SYS 612', 'SYS 671', 'SYS 800'], Remaining elective courses: ['SSW 540', 'SSW 565', 'SSW 810']", "Name: Fuller, E, Major: SYEN, Completed courses: ['SSW 540'], Remaining required courses: ['SYS 612', 'SYS 671', 'SYS 800'], Remaining elective courses: None"]
        output = [str(value) for key, value in repository.students_summary.items()]
        self.assertEqual(expected, output)

        expected = ["Name: Einstein, A, Dept: SFEN, Courses: ['SSW 567', 'SSW 540'], Students: [4, 2]", "Name: Feynman, R, Dept: SFEN, Courses: ['SSW 564', 'SSW 687', 'CS 501', 'CS 545'], Students: [3, 3, 1, 1]", "Name: Newton, I, Dept: SFEN, Courses: ['SSW 555', 'SSW 689'], Students: [1, 1]", 'Name: Hawking, S, Dept: SYEN, Courses: [], Students: []', 'Name: Edison, A, Dept: SYEN, Courses: [], Students: []', "Name: Darwin, C, Dept: SYEN, Courses: ['SYS 800', 'SYS 750', 'SYS 611', 'SYS 645'], Students: [1, 1, 2, 1]"]
        output = [str(value) for key, value in repository.instructors_summary.items()]
        self.assertEqual(expected, output)

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)