"""Demonstrates working with lists.
"""

from settings import *


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    imagine = ['Imagine', 1971, True, 'John Lennon']
    print(imagine)
    print()

    print(imagine[0])
    print(imagine[0:3])
    print(imagine[-2:])
    print()

    print(imagine == ['Imagine', 1971, True, 'John Lennon'])
    print(imagine is ['Imagine', 1971, True, 'John Lennon'])
    print()

    from datetime import date
    print(imagine + ['Klaus Voormann', date(1971, 10, 11)])
    print(imagine + ['Klaus Voormann', str(date(1971, 10, 11))])
    print()

    for item in (imagine + ['Klaus Voormann', str(date(1971, 10, 11))]):
        print(str(item))
    print()


def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    imagine = ['Imagine', 1971, True, 'John Lennon']

    # print(imagine.append('Klaus Voormann'))
    imagine.append('Klaus Voormann')
    print(imagine)
    print()

    from datetime import date
    imagine.insert(3, str(date(1971, 10, 11).strftime(PREFERRED_DATE_FORMAT)))
    print(imagine)
    print()

    imagine.remove(1971)
    print(imagine)
    print()

    imagine.pop(2)
    print(imagine)
    print()

    imagine.extend(('Klaus Voormann', str(date(1971, 10, 11).strftime(PREFERRED_DATE_FORMAT))))
    # imagine.extend('Ono')
    print(imagine)
    print()

    imagine.extend([1971, 1971])
    i = imagine.count(1971)
    print(imagine)
    print(i)
    print()

    print(imagine.index(1971))
    # print(imagine.index(1971, 0, len(imagine)))
    # print([i for i, v in enumerate(imagine)])
    print([i for i, v in enumerate(imagine) if imagine[i] == 1971])
    print()

    imagine.reverse()
    print(imagine)
    imagine.reverse()
    print()

    print(len(imagine))


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print(a)
    print(type(a))


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import seed, randint
    l = []
    seed(34)
    for i in range(1000):
        l.append(randint(1, 1001))
    print(l[23:34])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    imagine = ['Imagine', 1971, True, 'John Lennon']
    imagine2 = imagine.copy()
    imagine3 = imagine + []
    print(imagine == imagine2)
    print(imagine == imagine3)


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    l = [i for i in a]
    print(type(l))
    print(l)
    print()

    imagine = ['Imagine', '1971', 'John Lennon']
    print(', '.join(s for s in imagine))
    print()

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Knows']
    fw = [words[0] for words in [title.split() for title in songs]]
    # fw = [title.split()[0] for title in songs]                        # simpler (preferable)
    print(fw)
    # fw = [fw[0]] + [word for word in fw[1:]]
    print(' '.join([fw[0]] + [word.lower() for word in fw[1:]]))


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()

