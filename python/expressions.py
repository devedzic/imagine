"""Demonstrates how operators and expressions work in Python.
"""

from settings import *
from datetime import date


def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(((13 // 3) ** 2) % 5 - 2)


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    if 12 > 13:
        print('12 > 13')
    else:
        print('12 not > 13')
    print()

    d1 = date.today()
    d2 = date.today()
    if d1 == d2:
        print('d1 = d2')
    else:
        print('d1 != d2')
    print()

    print(id(d1))
    print(id(d2))
    print(d1 is d2)
    print()

    d1 = date(1971, 10, 11)
    d2 = date.today()
    if d1 > d2:
        print('d1 > d2')
    else:
        print('d1 not > d2')
    print()

    # a = None
    # try:
    #     print(d1 > a)
    # except:
    #     raise TypeError('My TypeError')
    # print(None)
    # print(type(None))
    # print(type(True))


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print(True and False)
    print(True and None)
    print(None or False)
    print(None or None)
    print()

    d1 = date(1971, 10, 11)
    print(d1 and None)
    print(d1 or None)
    if d1: print(d1)
    if 0.0: print(0.0)
    else: print('-----')
    print()

    # if None > d1: print()
    # print()


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

