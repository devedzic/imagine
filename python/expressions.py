"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print((45 // 12) % 3 - 200)


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(2 > 3)
    if 0:
        print(True)
    else:
        print(False)
    print()

    from datetime import date
    d1 = date(1971, 10, 11)
    d2 = date.today()

    if d1 > d2:
        print('d1 > d2')
    else:
        print('d2 >= d1')
    print()

    print(d1 is date(1971, 10, 11))
    print(d1 == date(1971, 10, 11))
    print('id(d1):', id(d1))
    print('id(d2):', id(d2))
    print()

    print(type(None))
    print(d1 == None)
    print(not None)
    print()


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    from datetime import date
    d1 = date(1971, 10, 11)
    d2 = date.today()

    print(True and False)
    print(True or False)
    print(True and not False)
    print(True and None)
    print(None or d1)
    print()

    print(1 and None)
    print(1 or None)
    print(1 or not None)
    print(not None)
    print()

    print(None or d1)
    # print(None > d1)
    print()


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

