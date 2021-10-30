"""Demonstrates peculiarities of if, for, while and other statements.
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    i1 = 'Imagine'
    i2 = 'Imagine'
    print(id(i1) == id(i2))
    print()

    i1 = ['Imagine']
    i2 = ['Imagine']
    print(id(i1) == id(i2))
    print()

    if 'II' in 'Imagine':
        print('II')
    elif 'y' in 'Imagine':
        print('y')
    elif 'x' in 'Imagine':
        print('x')
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

    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for c in 'Imagine'[3:]:
        print(c, end=' ')
    print()

    i = 0
    while i < 20:
        print(i, end= ' ')
        i += 1
    print()

    for _ in range(1, 5):
        print('Imagine')


if __name__ == '__main__':

    # demonstrate_branching()
    demonstrate_loops()
