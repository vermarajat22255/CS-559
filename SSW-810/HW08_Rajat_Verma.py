"""
HW08 implementation Python code to read files,
Analyze them using python and basic Date time Airthmatic
"""
from datetime import timedelta, datetime
from typing import IO, Tuple, Dict, Iterator, List
import os
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ perfoming arithmetic operation on dates """
    three_days_after_02272020: datetime = datetime(2020, 2, 27) \
        + timedelta(days=3)
    three_days_after_02272019: datetime = datetime(2019, 2, 27) \
        + timedelta(days=3)
    days_passed_02012019_09302019: int = (datetime(2019, 9, 30)
                                          - datetime(2019, 2, 1)).days
    return (three_days_after_02272020, three_days_after_02272019,
            days_passed_02012019_09302019)


def file_reader(path: str, fields: int, sep: str = ',',
                header: bool = False) -> Iterator[List[str]]:
    """ reading all the fields in a file using generator """
    try:
        file: IO = open(path, 'r')
    except BaseException:
        raise FileNotFoundError(f"File not found at {path}")
    else:
        line_nums = 0
        for line in file:
            line_nums += 1
            tokens: List[str] = line.strip().split(sep=sep)
            if len(tokens) != fields:
                file.close()
                raise ValueError(
                    f"ValueError: {path} has {len(tokens)} fields on \
                    line {line_nums} but expected {fields}")
            else:
                if header is False:
                    yield tokens
                else:
                    header = False


class FileAnalyzer:
    """ implement analyze_filers, pretty_print functions in this class
        Discussed aproach with Sanam Sritam Jena
    """

    def __init__(self, directory: str) -> None:
        """ initialize the vairable directory"""
        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ count number of lines, characters, functions and classes"""
        path: str = self.directory
        direct: List[str] = os.listdir(path)
        for f in direct:
            if f.endswith('.py'):
                try:
                    fp = open(os.path.join(path, f), 'r')
                except FileNotFoundError:
                    raise FileNotFoundError("Unable to open file!")
                else:
                    with fp:
                        character_count: int = 0
                        class_count: int = 0
                        function_count: int = 0
                        line_count: int = 0

                        for line in fp:
                            character_count += len(line)
                            line_count += 1

                            if line.strip().startswith('def '):
                                function_count += 1
                            if line.startswith('class '):
                                class_count += 1

                        self.files_summary[f] = {
                            'classes': class_count,
                            'functions': function_count,
                            'lines': line_count,
                            'characters': character_count
                        }

    def pretty_print(self) -> None:
        """ printing the table using pretty table """
        pretty_table: PrettyTable = PrettyTable(field_names=["File Name",
                                                             "Classes",
                                                             "Functions",
                                                             "Lines",
                                                             "Characters"])
        for file_name, props in self.files_summary.items():
            pretty_table.add_row([file_name, props["classes"],
                                  props["functions"],
                                  props["lines"], props["characters"]])
        print('\n summary for ', self.directory)
        print(pretty_table)


if __name__ == "__main__":
    test2 = FileAnalyzer('/home/india/Documents/python/SSW-810/HW4')
    test2.pretty_print()
