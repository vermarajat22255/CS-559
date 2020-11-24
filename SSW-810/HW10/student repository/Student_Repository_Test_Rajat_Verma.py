"""
@author: Rajat Verma
This file has a class named TestHW08 which has test cases
implemented to test functions defined in HW08_Tehreem_Tungekar.py
Namely, date_arithmetic(), file_reader(), analyze_files(), pretty_print()
"""

from datetime import datetime
import unittest

from Student_Repository_Rajat_Verma import date_arithmetic, file_reader, FileAnalyzer


class TestHW08(unittest.TestCase):
    """
    This class implements test case functions to test
    for functions implemented in HW Rajat Verma
    """
    def test_date_arithmetic(self) -> None:
        """
        This function has test cases for date_arithmetic()
        """
        self.assertEqual(
            date_arithmetic(),
            (datetime(2020, 3, 1), datetime(2019, 3, 2), 241))
        self.assertNotEqual(
            date_arithmetic(),
            (datetime(2020, 3, 1), datetime(2019, 3, 1), 21))

    def test_file_reader(self) -> None:
        """
        This function has test cases for file_reader()
        """
        expect = [['123', 'Jin He', 'Computer Science'],
                  ['234', 'Nanda Koka', 'Software Engineering'],
                  ['345', 'Benji Cai', 'Software Engineering']]
        self.assertEqual(list(file_reader('./student_majors.txt',
                                          3, '|', True)), expect)
        self.assertNotEqual(list(file_reader(
                                './student_majors.txt', 3, '|')), expect)
        with self.assertRaises(ValueError):
            list(file_reader('student_majors.txt', 4, '|', True))
        with self.assertRaises(FileNotFoundError):
            list(file_reader('xyz.txt', 3, '|', True))

    def test_analyze_files(self) -> None:
        """
        This function has test cases for analyze_files()
        """
        test = FileAnalyzer('./new fold')
        expected = {'abc.py':
                    {'classes': 1,
                     'functions': 1, 'lines': 3, 'characters': 44},
                    'two.py':
                    {'classes': 2, 'functions': 2, 'lines': 6,
                        'characters': 77}}
        self.assertEqual(test.files_summary, expected)
        with self.assertRaises(FileNotFoundError):
            FileAnalyzer(' ')

    def test_pretty_print(self) -> None:
        test2 = FileAnalyzer('/home/india/Documents/python/SSW-810/HW4')
        test2.pretty_print()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
