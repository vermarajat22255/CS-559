from HW03_Rajat_Verma import Fraction
import unittest

class TestFraction(unittest.TestCase):
    """ test class Fraction """

    def test_init(self) -> None: 
        """ function verifies that the numerator and denominator are set properly """
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f34.num, 3)
        self.assertEqual(f34.denom, 4)
    
    def test_str(self) -> None:
        """ Test function to test the str representation of Fraction"""
        f12: "Fraction" = Fraction(1, 2) 
        self.assertEqual(str(f12), "1/2")

    def test_init_exception(self) -> None: 
        with self.assertRaises(ValueError, msg="Invalid denominator"):
            f60: "Fraction" = Fraction(6, 0)

    def test_fraction_add(self) -> None: 
        """ test function for Fraction addition """
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertLess(f12+f34, Fraction(11,8))
        self.assertGreater(f12+f34, Fraction(9,8))
        

    def test_fraction_mul(self) -> None: 
        """ test Fraction multiply with more than two fractions"""
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f44: "Fraction" = Fraction(4, 4)
        self.assertEqual(f44 * f44 * f12, Fraction(50, 100))
        self.assertEqual(f12 + f34 * f44, Fraction(125, 100))
        self.assertLess(f12 + f34 * f44, Fraction(1, 2))


    def test_fraction_sub(self) -> None: 
        """ test function to test Fraction subtraction with more than two fractions"""
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-4, 16))
        self.assertEqual(f12 - f12 - f12, Fraction(-4, 8))
        self.assertNotEqual(f12 - f34 - f12, Fraction(-1, 16))
        self.assertEqual(f34, Fraction(3, 4))

    def test_fraction_mul(self) -> None: 
        """ test function to verify Fraction multiplication with more than two fractions"""
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        self.assertNotEqual(f12 * f12* f34, Fraction(3, 8))
        self.assertEqual(f12 * f12* f34, Fraction(3, 16))
        

    def test_fraction_div(self) -> None: 
        """ test function to verify Fraction division with more than 2 fractions"""
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f12 / f34 / f12, Fraction(8, 6))
        self.assertNotEqual(f12 / f12, Fraction(8, 6))

    def test_fraction_equal(self) -> None: 
        """ test function to verify Fraction equality"""
        f12: "Fraction" = Fraction(1, 2)
        f24: "Fraction" = Fraction(2, 4)
        f34: "Fraction" = Fraction(3, 4)
        f48: "Fraction" = Fraction(4, 8)
        self.assertTrue(f12 == f24 == f48)
        self.assertFalse(f48 == f34)

    def test_fraction_notequal(self) -> None: 
        """ test function to check Fraction inequality"""
        f12: "Fraction" = Fraction(1, 2)
        f45: "Fraction" = Fraction(4, 5)
        f34: "Fraction" = Fraction(3, 4)
        self.assertFalse(f12 == f45)
        self.assertTrue(f12 != f34)

    def test_fraction_lessthan(self) -> None: 
        """ test function to check Fraction less than """
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f44: "Fraction" = Fraction(4, 4)
        self.assertLess(f12, f44)
        self.assertTrue(f12 < f44)
    
    def test_fraction_lessthanequal(self) -> None: 
        """ test function check Fraction less than equal to """
        f12: "Fraction" = Fraction(1, 2)
        f44: "Fraction" = Fraction(4, 4)
        self.assertLessEqual(f12, f44)
        self.assertLessEqual(f12, f12)
        
    def test_fraction_greaterthan(self) -> None: 
        """ test function check Fraction greater than """
        f12: "Fraction" = Fraction(1, 2)
        f44: "Fraction" = Fraction(4, 4)
        self.assertGreater(f44, f12)
        
    def test_fraction_greaterthanequal(self) -> None: 
        """ This function verifies Fraction greater than equal to """
        f12: "Fraction" = Fraction(1, 2)
        f44: "Fraction" = Fraction(4, 4)
        self.assertGreaterEqual(f44, f12)
    
    def test_simplify(self):
        """
        test fractions for simplification
        """
        str1 = Fraction(100, 50).simplify().__str__()
        str2 = Fraction(2, 1).simplify().__str__()
        self.assertEqual(str1, str2)
        
        # negative numerators
        str3 = Fraction(-100, 50).simplify().__str__()
        str4 = Fraction(-2, 1).simplify().__str__()
        self.assertEqual(str3, str4)
        
        # negative denominator
        str5 = Fraction(100, -50).simplify().__str__()
        str6 = Fraction(2, -1).simplify().__str__()
        self.assertEqual(str5, str6)

        #fractions with both negative numbers
        str7 = Fraction(-100, -50).simplify().__str__()
        str8 = Fraction(2, 1).simplify().__str__()
        self.assertEqual(str7, str8)

        
        #  fractions for false cases
        str9 = Fraction(100, 50).simplify().__str__()
        str10 = Fraction(2, 3).simplify().__str__()
        self.assertNotEqual(str9, str10)

        #  fractions for false cases
        str11 = Fraction(100, 50).simplify().__str__()
        str12 = Fraction(-2, 1).simplify().__str__()
        self.assertNotEqual(str11, str12)

        # Testing fractions for false cases
        str13 = Fraction(-100, 50).simplify().__str__()
        str14 = Fraction(-2, -1).simplify().__str__()
        self.assertNotEqual(str13, str14)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)