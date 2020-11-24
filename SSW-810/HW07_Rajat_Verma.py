"""
author : Rajat Verma
Date November 11 2020
Write HW07 Class

"""
from collections import defaultdict, Counter
from typing import Any, DefaultDict, Optional, List, Set, Tuple
import string


class Homework07:
    """In this class, we will be creating all the functions required to solve HomeWork07
    """

    def __init__(self) -> None:
        """Initialise s with any type"""
        return None

    def anagrams_lst(self, str1: str, str2: str) -> bool:
        """checks the anagrams list"""
        if not isinstance(str1, str) or not isinstance(
                str2, str):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type String")
        return len(str1) == len(str2) and sorted(
            str1.lower()) == sorted(str2.lower())

    def anagrams_dd(self, str1: str, str2: str) -> bool:
        """ checks anagram using dictionary """
        if not isinstance(str1, str) or not isinstance(
                str2, str):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type String")

        dd: defaultdict[str, int] = defaultdict(int)
        for i in str1.lower():
            dd[i] += 1
        for ch in str2:
            if ch in dd and dd[ch] > 0:
                dd[ch] -= 1
            else:
                return False
        return not any(dd.values())

    def anagrams_cntr(self, str1: str, str2: str) -> bool:
        """ checks anagram using counter and returns boolean"""
        if not isinstance(str1, str) or not isinstance(
                str2, str):  # If the input is not of type 'Str', raise ValueError
            raise ValueError("Input l must be of type String")
        return Counter(str1) == Counter(str2)

    def covers_alphabet(self, sentence: str) -> bool:
        """checks if sentence has all the character
            https://stackoverflow.com/questions/59726206/how-are-these-sets-equal-eli5
        """
        if not isinstance(
                sentence,
                str):  # If the input is not of type 'Str', raise ValueError
            raise ValueError("Input sentence must be of type str")
        characters: Set = set()
        return set(string.ascii_lowercase) <= set(sentence.lower())

    def web_analyzer(
            self, weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
        """ web analyzer for web logs. dicussed with Sanam Jena"""

        if not isinstance(
                weblogs,
                List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input weblogs must be of type List")
        dd: DefaultDict[str, set[str]] = defaultdict(set)
        for names, webpage in weblogs:
            dd[webpage].add(names)
        return [(website, sorted(name))
                for website, name in sorted(dd.items())]
