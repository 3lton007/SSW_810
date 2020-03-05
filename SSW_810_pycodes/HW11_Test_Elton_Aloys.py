"""

@eltonlaoys

"""
import unittest
from HW10_Elton_Aloys import Student, Instructor, Repository


class StudentTest(unittest.TestCase):
    def test_student(self):
        """ Test Student summary table """
        student = Student("Elton Aloys", "Software Engineering")
        self.assertEqual(student.student_major, "Software Engineering")
        self.assertEqual(student.student_name, "Elton Aloys") 
        self.assertEqual(student.student_remaining_elective_courses, [])
        self.assertEqual(student.student_remaining_required_courses, [])
        self.assertEqual(student.student_completed_courses, [])


class InstructorTest(unittest.TestCase):
    def test_instructor(self):
        instructor = Instructor("James Rowland", "Software Engineering")
        self.assertEqual(instructor.instructor_name, "James Rowland")
        self.assertEqual(instructor.instructor_dept, "Software Engineering")
        self.assertEqual(instructor.instructor_courses_with_students, {})

class RepositoryTest(unittest.TestCase):
    """ Class test for Repository """
    def test_repository(self):
        repository = Repository("D:\PythonDev\.vscode")
        expected = {'SFEN': {'R': ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], 'E': ['CS 501', 'CS 513', 'CS 545']}, 'SYEN': {'R': ['SYS 612', 'SYS 671', 'SYS 800'], 'E': ['SSW 540', 'SSW 565', 'SSW 810']}}
        output = repository.majors_summary
        self.assertEqual(expected, output)

        instructors_lst = [["98764", "Cohen, R ", "SFEN", "SSW 546", 1],
                       ["98763", "Rowland, J", "SFEN", "SSW 810", 4],
                       ["98763", "Rowland, J", "SFEN", "SSW 555", 1],
                       ["98762", "Hawking, S", "CS", "SSW 501", 1],
                       ["98762", "Hawking, S", "CS", "CS 570", 1]]

        instructors_db = [("98762", "Hawking, S", "CS", "SSW 501", 1),
                          ("98764", "Cohen, R ", "SFEN", "SSW 546", 1),
                          ("98762", "Hawking, S", "CS", "CS 546", 1),
                          ("98762", "Hawking, S", "CS", "CS 570", 1),
                          ("98763", "Rowland, J", "SFEN", "SSW 555", 1),
                          ("98763", "Rowland, J", "SFEN", "SSW 810", 4)]

        #instructors_lst = [instructor_courses_with_students for line in path


        self.assertEqual(instructors_lst, instructors_db)



if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)  