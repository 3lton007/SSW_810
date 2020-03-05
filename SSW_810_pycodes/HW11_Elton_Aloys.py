"""

Creating a Data Repository of courses, students and instructors (HW09)
Adding Features to update signing up for next classes for next Semester (HW10)

@eltonaloysius

"""

from collections import defaultdict
import os
from prettytable import PrettyTable
import sqlite3

class Student:
    """ Initializing Student class with variables student_name, student_major and student_courses """
    def __init__(self, student_name, student_major):
        """ Function to initialize variable student_name, student_major and student_courses """
        self.student_name = student_name 
        self.student_major = student_major    
        self.student_completed_courses = list()
        self.student_remaining_required_courses = list()
        self.student_remaining_elective_courses = list()

    def __str__(self):
        return f"Name: {self.student_name}, Major: {self.student_major}, Completed Courses: {self.student_completed_courses}, Remaining required courses: {self.student_remaining_required_courses}, Remaining elective courses: {self.student_remaining_elective_courses}"

class Instructor:
    """ Initializing a Instructor class with variable instructor_name, instructor_dept, instructor_courses and instructor_students """
    def __init__(self, instructor_name, instructor_dept):
        """ Function to initialize variable instructor_name, instructor_dept, instructor_courses and instructor_students """
        self.instructor_name = instructor_name
        self.instructor_dept = instructor_dept
        self.instructor_courses_with_students = defaultdict(int) 

    def __str__(self):
        return f"Name: {self.instructor_name}, Dept: {self.instructor_dept}, Courses: {[key for key, value in self.instructor_courses_with_students.items()]}, Students: {[value for key, value in self.instructor_courses_with_students.items()]}"


class Repository:
    """ Repository for Data Structures """
    majors_summary = defaultdict(str)
    students_summary = defaultdict(str)
    instructors_summary = defaultdict(str)
    
    def __init__(self, directory):
        """ Function to initialize variable directory """
        self.directory = directory
        
    def read_files(self):
        """ Function to read all the files and create summary table """
        try:
            majors_file = open(os.path.join(self.directory, "majors.txt"))
            students_file = open(os.path.join(self.directory, "students.txt"))
            grades_file = open(os.path.join(self.directory, "grades.txt"))
            instructors_file = open(os.path.join(self.directory, "instructors.txt"))
            db_path = (os.path.join(self.directory, "810_data.db"))
        except FileNotFoundError:
            raise FileNotFoundError("File not Found / Cannot open File")
        else:
            """ Reading majors.txt file and populating majors_summary dictionary """
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
                    raise ValueError("Invalid elective Field ")

            """Reading students.txt file and adding student_summary in the dictionary""" 
            for cwid, name, major in self.file_reader(students_file, 3, "\t", False):
                self.students_summary[cwid] = Student(name, major)

            """Reading instructors.txt file and adding instructors_summary in the dictionary"""
            for cwid, name, dept in self.file_reader(instructors_file, 3, "\t", False):
                self.instructors_summary[cwid] = Instructor(name, dept)

            student_completed_courses = {}
            instructor_courses_with_students = {}
            """ Reading grades.txt file and populating student_completed_courses and instructor_courses_with_students dictionaries """
            for st_cwid, course, grade, in_cwid in self.file_reader(grades_file, 4, "\t", False):
                if grade.upper() == "F":
                    continue

                if st_cwid not in student_completed_courses:
                    student_completed_courses[st_cwid] = [course]
                else:
                    student_completed_courses[st_cwid].append(course)

                if in_cwid not in instructor_courses_with_students:
                    instructor_courses_with_students.update({in_cwid: {course: 1}})
                elif course not in instructor_courses_with_students[in_cwid]:
                    instructor_courses_with_students[in_cwid].update({course: 1})
                else:
                    instructor_courses_with_students[in_cwid][course] += 1

            """ Adding courses along with student count to Instructor object """
            for key, value in self.instructors_summary.items():
                try:
                    value.instructor_courses_with_students = instructor_courses_with_students[key]
                except KeyError:
                    print(f"{key} is not a valid course")

            """ Adding completed courses to students"""
            for key, value in student_completed_courses.items():
                try:
                    self.students_summary[key].student_completed_courses = sorted(value)
                except KeyError:
                    print(f"{key} not a valid course")


            for key, value in self.students_summary.items():
                value.student_remaining_required_courses = sorted(list(set(self.majors_summary[value.student_major]["R"]) - set(value.student_completed_courses)))
                value.student_remaining_elective_courses = sorted(list(set(self.majors_summary[value.student_major]["E"]) - set(value.student_completed_courses)))
                if len(value.student_remaining_elective_courses) < len(self.majors_summary[value.student_major]["E"]):
                    value.student_remaining_elective_courses = None

            try:
                connection = sqlite3.connect(db_path)
            except sqlite3.OperationalError:
                print(f" Error: Not be able top open {db_path}")
            else:
                cursor = connection.cursor()
                cursor.execute(""" Select i.CWID, i.name, i.Dept, g.Course, count(g.Course) as Students
                                    from instructors as i
                                    join grades as g on g.InstructorCWID = i.CWID
                                    group by g.Course, i.name
                                    """)
            result = cursor.fetchall()
            pt = PrettyTable(field_names=["CWID", 'Name', "Department", "Course", "No.of Students"])
            for value in result:
                pt.add_row(value)
            print(pt)

    def file_reader(self, fp, fields, sep = "\t", header = False):
        """ Generator that reads all the fields in the file """
        for offset, line in enumerate(fp, start = 1):
            if not header:
                header = True
                continue

            line = line.strip("\n").split(sep)

            if(len(line) != fields):
                print(f" The file has missing fields, {len(line)} fields present, needed {fields} on the {offset} in file {fp.name}")
            else:
                yield line


    def print_table(self):
        """ Function to print Summary Tables """
        self.read_files()

        """ Addind rows for major summary table """
        print("Major summary:")
        table = PrettyTable(field_names = ["Dept","Required","Electives"])

        for key,value in self.majors_summary.items():
            if key == "majors":
                continue
            table.add_row([key, value["R"], value["E"]])
        print(table)


        """ Adding rows to Summary Table """
        table = PrettyTable(field_names = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaing elective"])

        for key, value in self.students_summary.items():
            table.add_row([key, value.student_name, value.student_major, value.student_completed_courses, value.student_remaining_required_courses, value.student_remaining_elective_courses])
        print(table)


        """ Adding rows to instructor summary table """
        table = PrettyTable(field_names = ["CWID", "Name", "Dept", "Course", "Students"])
        
        for key, value in self.instructors_summary.items():
            for k, v in value.instructor_courses_with_students.items():
                table.add_row([key, value.instructor_name, value.instructor_dept, k, v])

        print(table)

    

def main():
    """ Function that creates an object of class Repository and prints both the tables """
    repository = Repository("D:\PythonDev\.vscode\HW11").print_table()

main()