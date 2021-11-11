"""Demonstrates sets.
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    # imagine =
    imagine = set()
    imagine.add('Imagine')
    print(type(imagine))
    print(imagine)
    imagine.update(['John Lennon', 1971])
    print(imagine)
    print()

    l = ['Imagine', 'John Lennon', 1971, 'Imagine']
    l = ('Imagine', 'John Lennon', 1971, 'Imagine')
    print(l)
    print(set(l))
    print(list(set(l)))
    print(tuple(set(l)))
    print()

    imagine.add('Imagine')
    print(imagine)
    print()

    print(imagine | set(('Alan White', 'Klaus Voormann')))
    print(imagine & {'Imagine', 1971})
    print(imagine - {1971})
    print(imagine ^ {1971, 'Imagine'})


if __name__ == '__main__':

    demonstrate_sets()

