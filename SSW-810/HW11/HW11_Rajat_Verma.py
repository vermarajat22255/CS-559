"""
Author : Rajat Verma
Created HW11 SSW810
"""

from typing import DefaultDict, Dict, List
import os
from prettytable import PrettyTable
from HW08_Rajat_Verma import file_reader
import sqlite3


class Major:
    """
    Class to Simulate the major of student
    """
    __slots__ = ['_major', '_required', '_electives']
    field_name: List[str] = ['Major', 'Required Course', 'Elective Course']

    def __init__(self, major: str) -> None:
        """
        initialise student using major
        """
        self._major: str = major
        self._required: List[str] = list()
        self._electives: List[str] = list()

    def add_course(self, required: str, course: str) -> None:
        """
        Add course to the student information
        """
        if required == 'R':
            self._required.append(course)
        elif required == 'E':
            self._electives.append(course)

    def get_required(self) -> List[str]:
        """
        Returns the list of required subjects
        """
        return list(self._required)

    def get_elective(self) -> List[str]:
        """
        Returns the list of elective subjects
        """
        return list(self._electives)

    def info(self) -> List[str]:
        """
        Returns the list of to be used in pretty table
        """
        return [self._major, self._required, self._electives]


class Student:
    """
        Simulate the behaviour of students in real world
    """
    field_name: List[str] = [
        'CWID',
        'Name',
        'Major',
        'Completed Courses',
        'Remaining Required',
        'Remaining Electives',
        'GPA']

    def __init__(
            self,
            cwid: str,
            name: str,
            major: str,
            required: List[str],
            electives: List[str]) -> None:
        """
        Initialize the Student object using relevent fields
        """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._required: List[str] = required
        self._electives: List[str] = electives
        self._grade: Dict[str, float] = {
            "A": 4.0, "A-": 3.75,
            "B+": 3.25, "B": 3.0, "B-": 2.75,
            "C+": 2.25, "C": 2.0, "C-": 0.0,
            "D+": 0.0, "D": 0.0, "D-": 0.0,
            "F": 0.0
        }
        self._course: Dict[str, str] = dict()
        self._course_fail: Dict[str, str] = dict()

    def course_add(self, course: str, grade: str) -> None:
        """
        Add the course using course and grade to the student information
        """
        if grade not in ["C-", "D+", "D", "D-", "F"]:
            self._course[course] = grade
        if grade in ["C-", "D+", "D", "D-", "F"]:
            self._course_fail[course] = grade
            return
        if course in self._required:
            self._required.remove(course)
        if course in self._electives:
            self._electives.clear()

    def compute_gpa(self) -> float:
        """
        Compute the GPA of student using the grade dictionary
        """
        sum_gpa: float = 0.0
        for grade in self._course.values():
            sum_gpa += self._grade[grade]
        for grade in self._course_fail.values():
            sum_gpa += self._grade[grade]
        if len(self._course) == 0:
            return 0.0
        return format(
            float((sum_gpa) / (len(self._course) + len(self._course_fail))), '.2f')

    def info(self) -> List[str]:
        """
        Returns the list of info for the pretty table
        """
        return [
            self._cwid, self._name, self._major, sorted(
                self._course .keys()), sorted(
                self._required), sorted(
                self._electives), self.compute_gpa()]


class Instructor:
    """
        Simulate the behaviour of Instructor in real world
    """
    field_name: List[str] = [
        "Cwid",
        "Name",
        "Department",
        "Course",
        "Students"]

    def __init__(self, cwid: str, department: str, name: str) -> None:
        """
        Initialise the Instructor with proper fields
        """
        self._cwid: str = cwid
        self._name: str = name
        self._department: str = department
        self._courses: Dict[str, int] = DefaultDict(int)

    def inst_add_course(self, course: str) -> None:
        """
        Add a course and the number of students in it to the dictionary
        """
        self._courses[course] += 1

    def info(self) -> List[str]:
        """
        Returns the list of required rows for pretty table
        """
        for i, j in self._courses.items():
            yield[self._cwid, self._name, self._department, i, j]


class Repository:
    """
        Simulate the Repository behavior to allow multiple university creation
    """

    def __init__(self, path: str, db_path: str) -> None:
        """
        Initialise the Repository from path using various files
        """
        self._path: str = path
        self._db_path: str = db_path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._majors: Dict[str, Major] = dict()
        self._read_majors()
        self._read_students()
        self._read_instructor()
        self._read_grades()
        self.major_pretty_table()
        self.student_pretty_table()
        self.instructor_pretty_table()
        self.student_grades_table(db_path)

    def _read_majors(self) -> None:
        """
        Read majors file from path construct object
        """
        try:
            path: str = os.path.join(self._path, "majors.txt")
            for major, required, course in file_reader(
                    path=path, fields=3, sep='\t', header=True):
                if major not in self._majors:
                    self._majors[major] = Major(major)
                self._majors[major].add_course(
                    required=required, course=course)
        except FileNotFoundError:
            print(f"Can not open file at {self._path}")
        except ValueError:
            print(" Some fields are missing in 1")

    def _read_students(self) -> None:
        """
        Read students file from path construct object
        """
        try:
            path: str = os.path.join(self._path, "students.txt")
            for cwid, name, major in file_reader(
                    path=path, fields=3, sep='\t', header=True):
                required: List[str] = self._majors[major].get_required()
                electives: List[str] = self._majors[major].get_elective()
                self._students[cwid] = Student(
                    cwid, name, major, required, electives)
        except FileNotFoundError:
            print(f"Can not open file at {self._path}")
        except ValueError:
            print(" Some fields are missing in 2 ")

    def _read_instructor(self) -> None:
        """
        Read instructor file from path construct object
        """
        try:
            path: str = os.path.join(self._path, "instructors.txt")
            for cwid, name, dept in file_reader(
                    path=path, fields=3, sep='\t', header=True):
                self._instructors[cwid] = Instructor(cwid, dept, name)

        except FileNotFoundError:
            print(f"Can not open file at {self._path}")
        except ValueError:
            print(" Some fields are missing in 3")

    def _read_grades(self) -> None:
        """Read grade file from path construct object"""
        try:
            path: str = os.path.join(self._path, "grades.txt")
            for stu_cwid, course, grade, inst_cwid in file_reader(
                    path=path, fields=4, sep='\t', header=True):
                if stu_cwid in self._students:
                    s: Student = self._students[stu_cwid]
                    s.course_add(course=course, grade=grade)
                else:
                    raise ValueError("No Student with such id")

                if inst_cwid in self._instructors:
                    p: Instructor = self._instructors[inst_cwid]
                    p.inst_add_course(course)
                else:
                    raise ValueError("No Professor with that ID")

        except FileNotFoundError:
            print(f"Can not open file at {self._path}")
        except ValueError:
            print(" Some fields are missing in 4")

    def major_pretty_table(self) -> PrettyTable:
        """
        Creating a pretty table
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Major.field_name
        for s in self._majors.values():
            pt.add_row(s.info())  # ["abc", [1,2,3], [4,5,6]]
        print(pt)
        return pt

    def student_pretty_table(self) -> PrettyTable:
        """
        Creating a pretty table of Student
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Student.field_name
        for s in self._students.values():
            pt.add_row(s.info())
        print(pt)
        return pt

    def instructor_pretty_table(self) -> PrettyTable:
        """
        Creating a pretty table of Instructor
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Instructor.field_name

        for instval in self._instructors.values():
            for row in instval.info():
                pt.add_row(row)
        print(pt)
        return pt

    def student_grades_table(self, db_path) -> PrettyTable:
        """
        Printing the query into a pretty table
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = ["Name", "CWID", "Course", "Grade", "Instructor"]
        try:
            db: sqlite3.Connection = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(e)
        else:
            try:
                for tup in db.execute(
                        "select s.Name, s.CWID, g.Course,  g.Grade, i.Name from student_majors s join grades g on s.CWID=StudentCWID join instructors i on InstructorCWID=i.CWID order by s.Name"):
                    pt.add_row(tup)
            except sqlite3.Error as e:
                print(e)
        print(pt)
        return pt


def main():
    stevens: Repository = Repository(
        "/home/india/Documents/python/SSW-810/HW11",
        r"/home/india/Documents/python/SSW-810/HW11/HomeWork11.db")


main()
