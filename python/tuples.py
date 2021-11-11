"""Demonstrates tuples.
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()
    print(type(empty_tuple))
    print(empty_tuple)
    one_tuple = (1,)
    print(one_tuple)
    pair = (1, 4, )
    print(pair)
    triplet = (1, 2, 6, )
    print(triplet)
    n_tuple = (True, 'Imagine', 1971)
    print(n_tuple)
    print(n_tuple[1])
    print()
    for i in n_tuple:
        print(i)
    # n_tuple[1] = '...'
    print()


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    imagine = 'Imagine', 'John Lennon', 1971,
    i, j, year = imagine
    print({i, j, year})
    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')

    theBeatles = zip(john, paul, george, ringo, )
    print(theBeatles)
    print(tuple(theBeatles))

    print()


if __name__ == '__main__':

    demonstrate_tuples()
    demonstrate_packing()
    demonstrate_zip()
