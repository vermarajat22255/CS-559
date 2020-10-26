from os import name
from typing import Iterator


class HomeWork:
    def reverse(self, s: str) -> str:
        """
        [This function reverse the String and return the reverse]
        Args:
            s (str): [description]
        Returns:
            str: [description]
        """
        
        reverse_str : str =""
        for i in s:
            reverse_str = i + reverse_str 
        return reverse_str

    def substring(self, target: str, s: str) -> int:
        """
        [This function return the substring ]

        Args:
            target (str): [target to be found]
            s (str): [String to be searched]

        Raises:
            ValueError: [if the value is not string]
        Returns:
            int:
        """
        if not isinstance(target, str):
            raise ValueError("Input must be of type string")
        if len(target) < 1:
            return 0
        if len(s) < 1:
            return -1
        for i in range(len(s)):
            if s[i:i+len(target)] == target:
                return i
        return -1
    
    def find_second(self, target: str, string: str) -> int:
        """
        [finds the second instance of the target in string]
        Args:
            target (str):
            string (str): 
        Returns:
            int:
        """
        startPosition: int = self.substring(target, string)
        out: int = string.find(target, startPosition+1)
        return out
    
    def get_lines(self, path: str) -> Iterator[str]:
        """[returns an Iterator that merges the lines on basis of conditions]

        Args:
            path (str): [path to file]

        Yields:
            Iterator[str]: [Iterator]
        """
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            print(f"Cant open {path}")
        else:
            with fp:
                # code is refered from Sanam sritam
                for line in fp:
                    line = line.rstrip('\n')
                    while line.endswith('\\'):
                        slashpointer: int = line.find('\\')
                        # was missing the space, so manually added the space
                        line = line[:slashpointer]+" "
                        line = line[:-1] + fp.readline().strip('\n')
                    # removing all lines starting with pound
                    line = line.split('#', 1)[0].strip('\n')
                    if line:
                        yield line
                    else:
                        continue

    def __init__(self, s:str ="") -> None:
        """[default initializer]
    
        Args:
            s (str): 

        Raises:
            ValueError: [is s is not string]
        """
        if not isinstance(s, str):
            raise ValueError("Input must be of type string")
        self.s = s
    
if __name__ == "__main__":
    hw:HomeWork  = HomeWork("")
    # hw.reverse(hw.s)
    # print(hw.substring('inas','omas'))
    # print(hw.find_second('iss','Mississippi'))
    print(hw.find_second('abba', 'abbabba'))