"""
Created on Sat oct 3 2020
by - Rajat Verma
"""


import random
import unittest
import HW04_Rajat_Verma
from typing import Iterator, List, Tuple
from HW04_Rajat_Verma import count_vowels, find_last
from HW04_Rajat_Verma import my_enumerate

# PART 1
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels """
        self.assertEqual(HW04_Rajat_Verma.count_vowels("in this sentance"),5)
        self.assertEqual(HW04_Rajat_Verma.count_vowels("Sly lynx fly by my crwth."),0)
        self.assertEqual(HW04_Rajat_Verma.count_vowels("Rajat verma"),4)
        self.assertNotEqual(HW04_Rajat_Verma.count_vowels("where"),3)
        
# PART 2
class FindLastTest(unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """
        self.assertEqual(HW04_Rajat_Verma.find_last( "l", "Hello" ) ,3)
        self.assertEqual(HW04_Rajat_Verma.find_last("butter",["Cured","jam","bread","butter","butter cups"]),3)
        self.assertEqual(HW04_Rajat_Verma.find_last("s","Hello"), None)
        self.assertNotEqual(HW04_Rajat_Verma.find_last("l","hello"),1)
        self.assertEqual(HW04_Rajat_Verma.find_last("not","l"), None)
    
# PART 3 is Fraction.simplify()

# PART 4

class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        str1:str=list(HW04_Rajat_Verma.my_enumerate([1,2,3]))
        str2:str=list(enumerate([1,2,3]))
        self.assertEqual(str1,str2)
        str1:str=list(HW04_Rajat_Verma.my_enumerate("Badshah honey"))
        str2:str=list(enumerate("Badshah"))
        self.assertNotEqual(str1,str2)
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)