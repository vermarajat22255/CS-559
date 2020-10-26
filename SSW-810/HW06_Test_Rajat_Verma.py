"""
Test case class to test the functions of the HW06 program
"""
import unittest
from HW06_Rajat_Verma import Operations, DonutQueue

class ListTest(unittest.TestCase):
    def test_list_copy(self)->None:
        """
        Test case to test list_copy
        """
        obj: Operations = Operations()
        self.assertEqual(obj.list_copy(list([-1,2,23])),list([-1,2,23]))
        self.assertEqual(obj.list_copy(list([])),list([]))
        self.assertNotEqual(obj.list_copy([1,1.2,"hello"]),[1,"two","hello"])
        with self.assertRaises(ValueError, msg="Input must be of type List"):
            obj.list_copy("")
        

    def test_list_intersect(self)->None:
        """
        Test case to test list_intersection
        """
        obj: Operations = Operations()
        self.assertEqual(obj.list_intersect(["egg","milk","cheese"],["wheat","bread","egg"]),["egg"])
        self.assertEqual(obj.list_intersect([1,2,3],[4,6,7]),[])
        self.assertEqual(obj.list_intersect([1,2,"three"],["three",6,7]),["three"])
        with self.assertRaises(ValueError, msg="Input must be of type List"):
            obj.list_intersect("",set())

    def test_list_difference(self)->None:
        """
        Test case to test list_difference
        """
        obj: Operations = Operations()
        self.assertEqual(obj.list_difference(["egg","milk","cheese"],["wheat","bread","egg"]),["milk","cheese"])
        self.assertEqual(obj.list_difference([1,2,3],[4,5,6]),[1,2,3])
        self.assertEqual(obj.list_difference([1,2,3],[1,2,3]),[])
        with self.assertRaises(ValueError, msg="Input must be of type List"):
            obj.list_difference(set(), [])
    
    def test_remove_vowels(self)->None:
        """
        Test case to test remove_vowels
        """
        obj: Operations = Operations()
        self.assertEqual(obj.remove_vowels("Amy is my favorite daughter"),"my favorite daughter")
        self.assertEqual(obj.remove_vowels("Jan is my best friend"),"Jan my best friend")
        self.assertEqual(obj.remove_vowels(""),"")
        with self.assertRaises(ValueError, msg="Input must be of type List"):
            obj.remove_vowels(list())
    
    def test_check_pwd(self)->None:
        """
        Test case to test check_pwd
        """
        obj: Operations = Operations()
        self.assertEqual(obj.check_pwd("8MyPass"),True)
        self.assertEqual(obj.check_pwd("711Sep"),False)
        self.assertEqual(obj.check_pwd("p@7ssword"),False)
        self.assertEqual(obj.check_pwd("7eVeN"),True)
        self.assertEqual(obj.check_pwd("@90"),False)
        self.assertEqual(obj.check_pwd(""),False)
        self.assertEqual(obj.check_pwd("1HELLO"),False)
        with self.assertRaises(ValueError, msg="Input must be of type List"):
            obj.check_pwd(9.2)

    def test_DonoutQueue(self)->None:
        """
        test case to test the working of DonutQueue class
        """
        queue: DonutQueue = DonutQueue()
        self.assertIsNone(queue.next_customer())
        queue.arrive("Sujit", False)
        queue.arrive("Fei", False)
        queue.arrive("Prof JR", True)
        self.assertEqual(queue.waiting(), "Prof JR, Sujit, Fei")
        queue.arrive("Nanda", True)
        self.assertEqual(queue.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(queue.next_customer(), "Prof JR")
        self.assertEqual(queue.next_customer(), "Nanda")
        self.assertEqual(queue.next_customer(), "Sujit")
        self.assertEqual(queue.waiting(), "Fei")
        self.assertEqual(queue.next_customer(), "Fei")
        self.assertIsNone(queue.next_customer())

if __name__ == "_main_":
    unittest.main(exit=False, verbosity=2)