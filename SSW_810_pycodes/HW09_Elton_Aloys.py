"""

Creating a Data Repository of courses, students and instructors
@eltonaloys

"""

from collections import defaultdict
import os
from prettytable import PrettyTable

class Student:
    """ Initializing Student class with variables student_name, student_major and student_courses """
    def __init__(self, student_name, student_major):
        """ Function to initialize variable student_name, student_major and student_courses """
        self.student_name = student_name 
        self.student_major = student_major    
        self.student_courses = []

    def __str__(self):
        return f"Name: {self.student_name}, Major: {self.student_major}, Courses: {self.student_courses}"

class Instructor:
    """ Initializing a Instructor class with variable instructor_name, instructor_dept, instructor_courses and instructor_students """
    def __init__(self, instructor_name, instructor_dept):
        """ Function to initialize variable instructor_name, instructor_dept, instructor_courses and instructor_students """
        self.instructor_name = instructor_name
        self.instructor_dept = instructor_dept
        self.instructor_courses = []
        self.instructor_students = 0

class Repository:
    """ A repository for Data Structures """
    def __init__(self, directory):
        """ Function to initialize variable directory """
        self.directory = directory
        
    def read_files(self):
        """ Function to read all the files and create summary table """
        try:
            students_file = open(os.path.join(self.directory, "students.txt"), "r")
            grades_file = open(os.path.join(self.directory, "grades.txt"), "r")
            instructors_file = open(os.path.join(self.directory, "instructors.txt"), "r")
        except FileNotFoundError:
            raise FileNotFoundError("Can't find/open files")
        else:
            self.students_summary = defaultdict(str)
            self.instructors_summary = defaultdict(str)

            for line in students_file:
                student_cwid, student_name, student_major = line.strip("\n").split("\t")
                self.students_summary[student_cwid] = Student(student_name, student_major)

            for line in instructors_file:
                instructor_cwid, instructor_name, instructor_dept = line.strip("\n").split("\t")
                self.instructors_summary[instructor_cwid] = Instructor(instructor_name, instructor_dept)

            for key, value in self.students_summary.items():
                for line in grades_file:
                    student_cwid, student_course, student_grade, instructor_cwid = line.strip("\n").split("\t")

                    self.instructors_summary[instructor_cwid].instructor_students += 1
                    self.instructors_summary[instructor_cwid].instructor_courses.append(student_course)
                    self.instructors_summary[instructor_cwid].instructor_courses = list(set(self.instructors_summary[instructor_cwid].instructor_courses))

                    if key == student_cwid:
                        value.student_courses.append(student_course)
                        value.student_courses.sort()                        
                    else:
                        self.students_summary[student_cwid].student_courses.append(student_course)
                        break                    

    def print_table(self):
        """ Function to print the two summary tables """
        self.read_files()

        table = PrettyTable(field_names = ["CWID", "Name", "Completed Courses"])
        for key, value in self.students_summary.items():
            table.add_row([key, value.student_name, value.student_courses])

        print(table)

        table = PrettyTable(field_names = ["CWID", "Name", "Dept", "Course", "Students"])
        for key, value in self.instructors_summary.items():
            for course in value.instructor_courses:
                table.add_row([key, value.instructor_name, value.instructor_dept, course, value.instructor_students])

        print(table)

def main():
    """ Function that creates an object of class Repository and prints both the tables """
    repository = Repository("C:\\Users\\Saksham\\Desktop\\810").print_table()

main()