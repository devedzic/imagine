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
    one_tuple = ('Imagine', )
    print(type(one_tuple))
    print(one_tuple)
    # two_tuple = ('Imagine', 'John Lennon')
    two_tuple = 'Imagine', 'John Lennon'
    print(type(two_tuple))
    print(two_tuple)
    three_tuple = 'Imagine', 'John Lennon', 1971
    print(three_tuple)
    print()

    print(three_tuple[1])
    # three_tuple[1] = 'JL'


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    two_tuple = 'Imagine', 'John Lennon'
    imagine, john = two_tuple
    print(two_tuple)
    print(imagine, john)
    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')

    theBeatles = zip(john, paul, george, ringo)
    print(theBeatles)
    print(list(theBeatles))
    print()

    theBeatles = zip(john, paul, george, ringo)                         # it is essential to re-create the zip object;
    for i, j, k, l in theBeatles:                                       # otherwise, this second loop prints nothing,
        print(str(i) + ';', str(j) + ';', str(k) + ';', str(l))         # (zip iterator exhausted in print(list(...)))
    print()


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_packing()
    demonstrate_zip()
