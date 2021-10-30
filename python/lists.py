"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    imagine = ['Imagine', 1971, True]
    print(imagine)
    print()

    print(imagine[0])
    print(imagine[0:-1])
    print()

    print(imagine == ['Imagine', 1971, True])
    print(imagine is ['Imagine', 1971, True])
    print(imagine + ['John Lennon', 'Klaus Voormann'])
    print()

    for item in (imagine + ['John Lennon', 'Klaus Voormann']):
        print(item)


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

    imagine = ['Imagine', 1971, True]
    print(imagine)
    print()

    print(imagine.append('John Lennon'))
    print(imagine)
    from datetime import date
    d = date(1971, 10, 11)
    imagine.insert(2, str(d))
    print(imagine)
    imagine.remove('1971-10-11')
    print(imagine)
    imagine.pop()
    print(imagine)
    imagine.append('John Lennon')
    imagine.pop(2)
    print(imagine)
    imagine.extend(['Imagine'])
    print(imagine)
    print(imagine.count('Imagine'))
    print(imagine.index('Imagine'))
    print([i for i in range(len(imagine)) if imagine[i] == 'Imagine'])
    imagine.reverse()
    print(imagine)
    imagine.reverse()
    print('John Lennon' in imagine)
    print('John Lennon' not in imagine)
    print()


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

    from random import randint, seed
    seed(23)
    l = []
    for i in range(1000):
        l.append(randint(0, 1000))
    print(l[34:56])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    imagine = ['Imagine', 1971, True]
    l = imagine
    print(imagine is l)
    l = imagine.copy()
    print(imagine is l)


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print([i for i in a])
    print([i for i in a if i % 2])
    print()

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Knows']
    print([song for song in songs if 'a ' in song])
    fw = [title.split()[0] for title in songs]
    print(fw)
    fw = fw[0].capitalize() + ' ' + ' '.join([item.lower() for item in fw[1:]])
    print(fw)
    print()

    imagine = ['Imagine', 'John Lennon', 1971, 'Imagine', 'Imagine']
    print([i for i, v in enumerate(imagine) if imagine[i] == 'Imagine'])


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()

