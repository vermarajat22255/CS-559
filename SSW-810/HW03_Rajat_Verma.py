"""
Created on Fri Sept 19 2020

@author: Rajat Verma

    Implement a class for fractions that supports addition, subtraction, multiplication, equals, and division
"""

class Fraction:
    """ Utility class to represent a Fraction Object and to Support basic operations on them like 
    addition, subtraction, multiplication, and division of fractions and checks for equality
    with a simple algorithm
    """
    __slots__ = ['num', 'denom', 'label']
    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise valueError on 0 denominator 
        """
        self.num : float = num
        self.denom: float = denom
        self.label : str = f"{self.num}/{self.denom}"
        if denom == 0:
            raise ValueError("denominator is invalid (0)")
        
    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{self.label}"
       
    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        num : float = (self.num * other.denom) + (self.denom * other.num)
        denom : float = (self.denom * other.denom)
        result: Fraction = Fraction(num, denom)
        return result
        
    def __sub__(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        num : float = (self.num * other.denom) - (self.denom * other.num)
        denom : float = (self.denom * other.denom)
        result: Fraction = Fraction(num, denom)
        return result
        
    def __mul__(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        num : float = (self.num * other.num)
        denom : float = (self.denom * other.denom)
        result: Fraction = Fraction(num, denom)
        return result
        
    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        num : float = (self.num * other.denom)
        denom : float = (self.denom * other.num)
        result: Fraction = Fraction(num, denom)
        return result
        
    def __eq__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are equivalent """
        return (self.num*other.denom) == (other.num * self.denom) 

    def __ne__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are not equivalent """
        return (self.num*other.denom) != (other.num * self.denom)
    
    def __lt__(self, other: "Fraction") -> bool:
        """ return True/False if the self is less than or equivalent """
        return (self.num*other.denom) < (other.num * self.denom)
    
    def __le__(self, other: "Fraction") -> bool:
        """ return True/False if self is less then equal to other fraction"""
        return (self.num*other.denom) <= (other.num * self.denom)
    
    def __gt__(self, other: "Fraction") -> bool:
        """ return True/False if self is greater than other fraction"""
        return (self.num*other.denom) > (other.num * self.denom)
    
    def __ge__(self, other: "Fraction") -> bool:
        """ return True/False if self is greater then __eq__ to other fraction"""
        return (self.num*other.denom) >= (other.num * self.denom)

class Helper:
    """ 
    Helper class to call and utilize function in utility class i.e. Fraction
    """
    __slots__ = []
    def test_suite(self) -> None:
        """ 
        test suites to check the behaviour of the functions
        """
        try:
            f12: Fraction = Fraction(1, 2)
            f34: Fraction = Fraction(3, 4)
            f68: Fraction = Fraction(6, 8)
            f128: Fraction = Fraction(12, 8)
            f32: Fraction = Fraction(3, 2)
            f912: Fraction = Fraction(9, 12)
            f44: Fraction = Fraction(4, 4)    

            # Required Test Cases
            print("Required test cases \n")
            print(f"{f12} + {f12} = {f12.__add__(f12)} [4/4]")
            print(f"{f44} - {f12} = {f44.__sub__(f12)} [4/8]")
            print(f"{f12} + {f44} = {f12.__add__(f44)} [12/8]")
            print(f"{f128} == {f32} is {f128.__eq__(f32)} [True]")

            # Custom test Cases

            print("Custom test cases \n")
            print(f"{f12} + {f34} = {f12.__add__(f34)} [10/8]")
            print(f"{f12} + {f34} + {f44} = {f12.__add__(f34).__add__(f44)} [72/32]")
            print(f"{f12} * {f34} + {f44} = {f12.__mul__(f34).__add__(f44)} [44/32]")
            print(f"{f12} / {f34}  ==  {f44} = {f12.__truediv__(f34).__eq__(f44)} [False]")
            print(f"{f128} + {f68} - {f44} = {f128.__add__(f68).__sub__(f44)} [320/256]")
            print(f"{f128} [12/8]")
        except ValueError:
            print(" Zero division error encountered, check the following- ", ValueError)
        except BaseException:
            print("Something went wrong, check more Info at "+BaseException)

    def get_number(self, prompt: str) -> float:
        """ read and return a number from the user.
            Loop until the user provides a valid number.
        """
        while True:
            inp: str = input(prompt)
            try:
                return float(inp)
            except ValueError:
                print(f"Error: '{inp}' is not a number. Please try again...")

    def get_fraction(self) -> Fraction:
        """ Ask the user for a numerator and denominator and return a valid Fraction """
        
        while True:
            num: float = self.get_number("Enter the numerator of Fraction: ")
            denom: float = self.get_number("Enter the Denominator(Non zero) of Fraction :")
            try:
                f1 : Fraction = Fraction(num, denom)
            except ValueError:
                print(f"Denominator is 0, please enter valid Fraction again.")
            except BaseException:
                print(f"Something went wrong !! more info here -> {BaseException}\n Try Again!!!\n")
            else:
                return f1
        
    def compute(self, f1: Fraction, operator: str, f2: Fraction) -> None:
        """ Given two fractions and an operator, return the result
            of applying the operator to the two fractions
        """
        result: Fraction  # just define the type of result, don't set a value
        is_fraction: bool = True

        if operator == '+':
            result = f1 + f2
        elif operator == '-':
            result = f1 - f2
        elif operator == '*':
            result = f1 * f2
        elif operator == '/':
            result = f1/ f2
        elif operator == ">":
            print(f"{f1.__gt__(f2)}")
            is_fraction = False
        elif operator == ">=":
            print(f"{f1.__ge__(f2)}")
            is_fraction = False
        elif operator == "<":
            print(f"{f1.__lt__(f2)}")
            is_fraction = False
        elif operator == "<=":
            print(f"{f1.__le__(f2)}")
            is_fraction = False
        elif operator == "!=": 
            print(f"{f1.__ne__(f2)}")
            is_fraction = False   
        elif operator == '==':
            print(f"{f1} {operator} {f2} = {f1.__eq__(f2)}")
            is_fraction=False
        else:
            print(f"Error: '{operator}' is an unrecognized operator")
            is_fraction = False

        if is_fraction:
            print(f"{f1} {operator} {f2} = {result}")

def main() -> None:
    """ Fraction calculations """
    print("***********Starting Test Suites***************")
    helper: Helper = Helper()   # create a helper reference to access the helper functions
    helper.test_suite()         # call test suite using helper
    print("***********Finished Test Suites***************\n")
    print('Welcome to the fraction calculator!')
    f1: Fraction = helper.get_fraction()    # call functions of helper to get access of utility class
    operator: str = input("Operation (+, -, *, /, ==, !=, >, >=, <, <=): ")
    f2: Fraction = helper.get_fraction()
    
    try:
        helper.compute(f1, operator, f2)    # compute the result using utility class by helper class
    except ValueError as e:
        print("\nYou have entered a 0 in denominator, Invalid expressiom !! Try Again  \n", e)
    except Exception as common:
        print("Can not process computation -",common)

if __name__ == '__main__':
    main()