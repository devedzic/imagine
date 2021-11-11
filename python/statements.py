"""Demonstrates peculiarities of if, for, while and other statements.
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    imagine = ['Imagine', 1971]

    if imagine == ['Imagine', 1971]:
        print(True)
    if imagine is ['Imagine', 1971]:
        print(True)
    else:
        print(False)
    if imagine:
        print(True)
    print()

    n = 4
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        print(None)


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    l = [1, 2, 3, 4, 5, 6, 7]
    for i in l[2:-3]:
        print(i)
    print()
    for i in range(1, 12, 2):
        print(i)
    print()
    for _ in range(1, 12, 2):
        print('Imagine')
    print()
    i = 0
    while i < 10:
        print(i)
        i += 1


if __name__ == '__main__':

    demonstrate_branching()
    demonstrate_loops()
