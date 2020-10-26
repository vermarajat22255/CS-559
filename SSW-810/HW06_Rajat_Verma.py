
from typing import Any, Optional, List
class Operations:
    """In this class, we will be creating all the functions required to solve HomeWork06
    """

    def __init__(self) -> None:
        """Initialise s with any type"""
        return None

    def list_copy(self, l: List[Any]) -> List[Any]:
        """Copies the given list and return a clone"""
        if not isinstance(l, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type List")
        return [i for i in l]

    def list_intersect(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        """ return the list all the element that are present in both the list"""
        if not isinstance(l1, List) or not isinstance(l2, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type List")
        return [i for i in l1 if i in l2]
        
    def list_difference(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        """ returns the elements in l1 that are Not in l2"""
        if not isinstance(l1, List) or not isinstance(l2, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type List")
        return [i for i in l1 if i not in l2]
    
    def remove_vowels(self, input: str) -> str:
        """ remove the words from the given string that starts with Vowels"""
        if not isinstance(input, str):  # If the input is not of type 'String', raise ValueError
            raise ValueError("Input l must be of type String")
        return " ".join([i for i in input.split() if i[0] not in ['a','e','i','o','u','A','E','I','O','U']])
    
    def check_pwd(self, password: str) -> bool:
        """ checks the password for given three conditions, returns true or false"""
        if not isinstance(password, str):  # If the input is not of type 'String', raise ValueError
            raise ValueError("Input l must be of type String")
        return len(password) >= 4 and password[0].isdigit() \
            and len([i for i in password[1:] if i.isupper()]) >=2 \
            and len([i for i in password[1:] if i.islower()] ) >= 1

class DonutQueue:
    """ Donut Queue class implements the functionality of regular queues with priority set via VIP"""
    queue: List
    def __init__(self ) -> None:
        """Initialise and empty queue"""
        self.queue: List = []
    
    def __str__(self ) -> str:
        """ regular string representation of the queue, returns name of the person in queue"""
        return ", ".join([i[0] for i in self.queue]) if len(self.queue) > 0 else "None"
    
    def arrive(self, name: str, vip: bool) -> None:
        """ function that emulates the customer insertion in a queue"""
        if len(self.queue) == 0:
            self.queue.append([name, vip])
            return
        if vip:
            for index,person in enumerate(self.queue):
                if not person[1]:
                    self.queue.insert(index, [name, vip])
                    break
        else:
            self.queue.append([name, vip])

    def next_customer(self) -> Optional[str]:
        """ returns the name of the first person in the queue, None if queue is empty """
        return None if len(self.queue)<1 else self.queue.pop(0)[0]

    def waiting(self) -> Optional[str]:
        """ returns the string representation of the queue i.e people name waiting in the queue"""
        return str(self)