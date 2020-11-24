"""
Author: Rajat Verma
write test class for HW07 class
"""
from typing import List, Tuple
from HW07_Rajat_Verma import Homework07
import unittest


class HW07_Test_Rajat_Verma(unittest.TestCase):
    """Test class to validate functions"""

    def test_anagrams_lst(self) -> None:
        """ In this function, we will be testing the anagrams_lst function from HomeWork07 class """
        test: Homework07 = Homework07()
        self.assertEqual(test.anagrams_lst("Dirtyroom", "Dormitory"), True)
        self.assertEqual(test.anagrams_lst("Cinema", "Iceman"), True)
        self.assertEqual(test.anagrams_lst("hands", "sandh"), True)
        self.assertEqual(test.anagrams_lst("Name", "Fame"), False)
        self.assertEqual(test.anagrams_lst("", ""), True)
        self.assertEqual(test.anagrams_lst("tom cat", "tomc at"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_lst(1, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of type str"):
            test.anagrams_lst("Dormitory", 0)

    def test_anagrams_defaultdict(self) -> None:
        """In this function, we will be testing the anagrams_dd function from HomeWork07 class.
        """
        test: Homework07 = Homework07()
        self.assertEqual(test.anagrams_lst("Dirtyroom", "Dormitory"), True)
        self.assertEqual(test.anagrams_lst("Cinema", "Iceman"), True)
        self.assertEqual(test.anagrams_lst("hands", "sandh"), True)
        self.assertEqual(test.anagrams_lst("Name", "Fame"), False)
        self.assertEqual(test.anagrams_lst("", ""), True)
        self.assertEqual(test.anagrams_lst("tom cat", "tomc at"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_lst(1, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of type str"):
            test.anagrams_lst("Dormitory", 0)

    def test_anagrams_cntr(self) -> None:
        """In this function, we will be testing the anagrams_cntr function from HomeWork07 class.
        """
        test: Homework07 = Homework07()
        self.assertEqual(test.anagrams_lst("Dirtyroom", "Dormitory"), True)
        self.assertEqual(test.anagrams_lst("Cinema", "Iceman"), True)
        self.assertEqual(test.anagrams_lst("hands", "sandh"), True)
        self.assertEqual(test.anagrams_lst("Name", "Fame"), False)
        self.assertEqual(test.anagrams_lst("", ""), True)
        self.assertEqual(test.anagrams_lst("tom cat", "tomc at"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_lst(1, "Dormitory")
        with self.assertRaises(ValueError):
            test.anagrams_lst("Dormitory", 1)

    def test_covers_alphabet(self) -> None:
        """In this function, we will be testing the test_covers_alphabet function from HomeWork07 class.
        """
        test: Homework07 = Homework07()
        self.assertEqual(test.covers_alphabet(
            "qwertyuiopasdfghjklzxcvbnm"), True)
        self.assertEqual(test.covers_alphabet(
            "We promptly judged antique ivory buckles for the next prize"), True)
        self.assertEqual(test.covers_alphabet("xyz"), False)
        with self.assertRaises(ValueError):
            test.covers_alphabet(0)

    def test_web_analyzer(self) -> None:
        """In this function, we will be testing the test_web_analyser function from HomeWork07 class.
        """
        test: Homework07 = Homework07()
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(test.web_analyzer(weblogs), summary)

        with self.assertRaises(ValueError):
            test.web_analyzer(0)
