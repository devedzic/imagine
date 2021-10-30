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

    # imagine = {}            # No, it's an empty dict, not an empty set!
    # print(type(imagine))
    imagine = set()
    print(imagine)
    print(type(imagine))
    imagine.add('Imagine')
    print(imagine)
    print()

    theBeatles = {'John', 'Paul', 'George', 'Ringo'}
    print(type(theBeatles))
    print(theBeatles)
    print(id(theBeatles))
    theBeatles.add('Brian')
    print(theBeatles)
    print(id(theBeatles))
    imagine.add('George')
    print(theBeatles)          # No duplicates
    print()

    for m in theBeatles:
        print(m)
    print()

    print(theBeatles - {'Brian'})
    print(theBeatles & {'Brian', 'Paul'})
    print(theBeatles)
    print(theBeatles | {'Stewart', 'Pete'})
    print(theBeatles ^ {'Stewart'})


if __name__ == '__main__':

    demonstrate_sets()

