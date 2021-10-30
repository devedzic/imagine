"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""

from settings import *


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    d1 = {}
    d2 = dict()
    print(type(d1))
    print(type(d2))
    print(d1, d2)
    print()

    imagine = {'title': 'Imagine', 'year': 1971, 'famous': True}
    print(imagine)
    print()

    print(imagine['title'])
    print()

    print(imagine.items())
    print(list(imagine.items()))
    for k, v in list(imagine.items()):
        print(str(k) + ':', v)
    print()

    from pprint import pprint
    pprint(imagine)
    pprint(imagine, width=1)
    print()

    imagine['dominant_instrument'] = 'piano'
    pprint(imagine)
    imagine.pop('dominant_instrument')
    # i = imagine.pop('dominant_instrument')
    # print(i)
    pprint(imagine)
    print()

    from datetime import date
    dates = {'recorded': date(1971, 5, 27), 'released': date(1971, 10, 11)}
    # dates = {'recorded': date(1971, 5, 27).strftime(PREFERRED_DATE_FORMAT),
    #          'released': date(1971, 10, 11).strftime(PREFERRED_DATE_FORMAT)}
    imagine.update(dates)
    pprint(imagine)
    imagine.update([('author', 'John Lennon')])
    pprint(imagine)
    print()

    print(imagine.keys())
    print(imagine.values())
    print(list(imagine.keys()))
    print(list(imagine.values()))
    print([(k, v) for k, v in zip(imagine.keys(), imagine.values())])
    print()


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter
    # if by == 'k' or by == 'K':
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    # from operator import itemgetter
    if by == 'k' or by == 'K':
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif by == 'v' or by == 'V':
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    # imagine = {'title': 'Imagine', 'year': 1971, 'famous': True}
    imagine = {'title': 'Imagine', 'year': '1971', 'famous': 'True'}
    print(sort_dictionary(imagine, 'k'))
    print(sort_dictionary(imagine, 'v'))    # raises TypeError if values are not comparable (e.g. int and str)
    print(sort_dictionary(imagine, 23))


if __name__ == '__main__':
    # demonstrate_dictionaries()
    demonstrate_dict_sorting()

    # print(globals())
    # print(demonstrate_dictionaries.__globals__)
