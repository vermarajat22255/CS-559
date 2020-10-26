"""
Author: Sanam Jena
CWID:10454295
Date: 10 October 2020
Objective: To write test class for HW05
"""
from typing import List, Iterator
import unittest
from HW05_Rajat_Verma import HomeWork


class HomeWorkTest(unittest.TestCase):
    """Testing the Reverse function"""

    def test_reverse(self) -> None:
        """ 
        test to check the reverse function
        """
        test: HomeWork = HomeWork("reverse")
        self.assertEqual(test.s, "reverse")  # Checking if init works
        
        # Checking if reverse works
        self.assertEqual(test.reverse(test.s), "esrever")
        
        # checking for a palindrome
        test1: HomeWork = HomeWork("codedoc")
        self.assertEqual(test1.reverse(test1.s), "codedoc")
        test2: HomeWork = HomeWork("x")
        self.assertEqual(test2.reverse(test2.s), "x")
        test3: HomeWork = HomeWork("abc")
        self.assertNotEqual(test3.reverse(test3.s), "abc")
        test4: HomeWork = HomeWork(" ")
        self.assertEqual(test4.reverse(test4.s), " ")
        with self.assertRaises(ValueError, msg="Input must be of type string"):
            test5: HomeWork = HomeWork(55)
        
    def test_substring(self) -> None:
        """
        function to verify the substring function
        """
        test: HomeWork = HomeWork("This is a line which contains test words")
        self.assertEqual(test.substring("line", test.s), 10)
        self.assertEqual(test.substring("contains", test.s), 21)
        self.assertEqual(test.substring("is", test.s), 2)
        self.assertEqual(test.substring("XYZ", ""), -1)
        self.assertEqual(test.substring("", test.s), 0)
        self.assertEqual(test.substring("", ""), 0)

    def test_find_second(self) -> None:
        """function to test the "find_second" function.
        """
        test1: HomeWork = HomeWork("Mississippi")
        self.assertEqual(test1.find_second("iss", test1.s), 4)
        self.assertEqual(test1.find_second("xyz", test1.s), -1)
        
        test2: HomeWork = HomeWork("finding the second word in between words")
        self.assertEqual(test2.find_second("word", test2.s), 35)
        
        test3: HomeWork = HomeWork("finding the second word in between words")
        self.assertEqual(test3.find_second("words", test3.s), -1) 
        
        test4: HomeWork = HomeWork("finding the second word in between words")
        self.assertNotEqual(test4.find_second("", test4.s), 35)

    def test_get_lines(self) -> None:
        """In this function, we will be testing the get_lines function.
        """
        test: HomeWork = HomeWork("")
        file_name = '/home/india/Documents/python/test1.txt'
        expect: List[str] = ['<line0>', '<line1>', '<line2>','<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(test.get_lines(file_name))
        self.assertEqual(result, expect)

        # Testing for empty file
        test2: HomeWork = HomeWork("")
        file_name_2 :str = '/home/india/Documents/python/test2.txt'
        expect1: List[str] = []
        result1: List[str] = list(test2.get_lines(file_name_2))
        self.assertEqual(result1, expect1)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)