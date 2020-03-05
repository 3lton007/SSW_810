"""
    Python program that creates a repository for a university
    Author: Saksham Tiwari
    Date: 10/30/2019 12:18
"""

from collections import defaultdict
import os
from prettytable import PrettyTable

class Student: 
    """ Class that initializes variable variable student_name, student_major and student_courses """
    def __init__(self, student_name, student_major, student_completed_courses = [], student_remaining_required_courses = [], student_remaining_elective_courses = []):
        """ Function to initialize variable student_name, student_major and student_courses """
        self.student_name = student_name 
        self.student_major = student_major    
        self.student_completed_courses = student_completed_courses
        self.student_remaining_required_courses = student_remaining_required_courses
        self.student_remaining_elective_courses = student_remaining_elective_courses

    def __str__(self):
        return f"Name: {self.student_name}, Major: {self.student_major}, Completed courses: {self.student_completed_courses}, Remaining required courses: {self.student_remaining_required_courses}, Remaining elective courses: {self.student_remaining_elective_courses}"

class Instructor:
    """ Class that initializes variable instructor_name, instructor_dept, instructor_courses and instructor_students """
    def __init__(self, instructor_name, instructor_dept, instructor_courses_with_students = defaultdict(int)):
        """ Function to initialize variable instructor_name, instructor_dept, instructor_courses and instructor_students """
        self.instructor_name = instructor_name
        self.instructor_dept = instructor_dept
        self.instructor_courses_with_students = instructor_courses_with_students

    def __str__(self):
        return f"Name: {self.instructor_name}, Dept: {self.instructor_dept}, Courses: {[key for key, value in self.instructor_courses_with_students.items()]}, Students: {[value for key, value in self.instructor_courses_with_students.items()]}"

class Repository:
    """ Class that reads, summarizes and prints the required summaries """
    majors_summary = defaultdict(str)
    students_summary = defaultdict(str)
    instructors_summary = defaultdict(str)

    def __init__(self, directory):
        """ Function to initialize variable directory """
        self.directory = directory
        
    def read_files(self):
        """ Function to read both the files and create the required summaries """
        try:
            majors_file = open(os.path.join(self.directory, "majors.txt"), "r")
            students_file = open(os.path.join(self.directory, "students.txt"), "r")
            grades_file = open(os.path.join(self.directory, "grades.txt"), "r")
            instructors_file = open(os.path.join(self.directory, "instructors.txt"), "r")
        except FileNotFoundError:
            raise FileNotFoundError("Can't find/open files")
        else:
            # Reading majors.txt file and populating majors_summary dictionary
            for major, required_elective, course in self.file_reader(majors_file, 3, "\t", False):
                if len(self.majors_summary[major]) == 0:
                        self.majors_summary[major] = {}

                if required_elective.upper() == "R":                    
                    if required_elective not in self.majors_summary[major]:
                        self.majors_summary[major][required_elective] = [course]
                    else:
                        self.majors_summary[major][required_elective].append(course)
                        self.majors_summary[major][required_elective].sort()
                elif required_elective.upper() == "E":
                    if required_elective not in self.majors_summary[major]:
                        self.majors_summary[major][required_elective] = [course]
                    else:
                        self.majors_summary[major][required_elective].append(course)
                        self.majors_summary[major][required_elective].sort()
                else:
                    raise ValueError("Invalid Required/Elective field ")

            # Reading students.txt file and populating students_summary dictionary
            for cwid, name, major in self.file_reader(students_file, 3, ";", False):
                self.students_summary[cwid] = Student(name, major)

            # Reading instructors.txt file and populating instructors_summary dictionary
            for cwid, name, dept in self.file_reader(instructors_file, 3, "|", False):
                self.instructors_summary[cwid] = Instructor(name, dept)

            student_completed_courses = {}
            instructor_courses_with_students = {}
            # Reading grades.txt file and populating student_completed_courses and instructor_courses_with_students dictionaries
            for s_cwid, course, grade, i_cwid in self.file_reader(grades_file, 4, "|", False):
                if grade.upper() == "F":
                    continue

                if s_cwid not in student_completed_courses:
                    student_completed_courses[s_cwid] = [course]
                else:
                    student_completed_courses[s_cwid].append(course)

                if i_cwid not in instructor_courses_with_students:
                    instructor_courses_with_students.update({i_cwid: {course: 1}})
                elif course not in instructor_courses_with_students[i_cwid]:
                    instructor_courses_with_students[i_cwid].update({course: 1})
                else:
                    instructor_courses_with_students[i_cwid][course] += 1

            # Adding courses along with student count to each Instructor object
            for key, value in self.instructors_summary.items():
                try:
                    value.instructor_courses_with_students = instructor_courses_with_students[key]
                except KeyError:
                    continue

            # Adding completed courses to each Student object
            for key, value in student_completed_courses.items():
                try:
                    self.students_summary[key].student_completed_courses = sorted(value)
                except KeyError:
                    continue

            # Adding remaining required and elective courses to each Student object
            for key, value in self.students_summary.items():
                value.student_remaining_required_courses = sorted(list(set(self.majors_summary[value.student_major]["R"]) - set(value.student_completed_courses)))
                value.student_remaining_elective_courses = sorted(list(set(self.majors_summary[value.student_major]["E"]) - set(value.student_completed_courses)))
                if len(value.student_remaining_elective_courses) < len(self.majors_summary[value.student_major]["E"]):
                    value.student_remaining_elective_courses = None
            
    def file_reader(self, fp, fields, sep = "|", header = False):
        """ Generator that reads all the fields in the file """
        for offset, line in enumerate(fp, start = 1):
            if not header:
                header = True
                continue

            line = line.strip("\n").split(sep)

            if(len(line) != fields):
                raise ValueError(f"The file has missing fields, {len(line)} fields present, needed {fields} on line {offset} in file {fp.name}")
            else:
                yield line

    def print_table(self):
        """ Function to print the two summary tables """
        self.read_files()

        # Adding rows to major summary table
        print("Major summary:")
        table = PrettyTable(field_names = ["Dept", "Required", "Electives"])

        for key, value in self.majors_summary.items():
            if key == "Major":
                continue
            table.add_row([key, value["R"], value["E"]])

        print(table)

        # Adding rows to student summary table
        print("Student summary:")
        table = PrettyTable(field_names = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Elective"])

        for key, value in self.students_summary.items():
            table.add_row([key, value.student_name, value.student_major, value.student_completed_courses, value.student_remaining_required_courses, value.student_remaining_elective_courses])

        print(table)

        # Adding rows to instructor summary table
        print("Instructor summary:")
        table = PrettyTable(field_names = ["CWID", "Name", "Dept", "Course", "Students"])

        for key, value in self.instructors_summary.items():
            for k, v in value.instructor_courses_with_students.items():
                table.add_row([key, value.instructor_name, value.instructor_dept, k, v])

        print(table)

def main():
    """ Function that creates an object of class Repository and prints both the tables """
    repository = Repository("C:\\Users\\Saksham\\Desktop\\810\\SSW-810").print_table()

main()