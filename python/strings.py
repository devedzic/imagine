"""Demonstrates working with strings in Python.
"""

import string

import settings


def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('%7.7f, %d, %s' % (2.3, 3, 'Imagine'))
    print('c:\nowhere man')
    print(r'c:\nowhere man')
    print(
"""He's a real nowhere man
Sitting in his nowhere land
Making all his nowhere plans 
for nobody""")
    print('nowhere          ' * 3)
    print('nowhere'[:])
    print('nowhere'[:3])
    print('nowhere'[:-3])
    print('nowhere'[-3:])


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    song = 'Imagine'
    author = 'John Lennon'
    year = 1971
    # print('{}, a song by {} ({})'.format('Imagine', 'John Lennon', 1971))
    print('{}, a song by {} ({})'.format(song, author, year))


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    song = 'Imagine'
    author = 'John Lennon'
    year = 1971
    print(f'{song}, a song by {author} ({year})')


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...), strip() (lstrip(), rstrip())
    """

    imagine = 'Imagine, a song by John Lennon.'

    print(imagine.startswith('Imagine'))
    print(imagine.startswith('imagine'))
    print(imagine.endswith('imagine'))
    print(imagine.endswith('.'))
    print()

    print('Imagine'.center(30, '*'))
    # print('Imagine'.center(5, '*'))
    print('Imagine' in imagine)
    print('Imagine' == imagine)
    print(len(imagine))
    print()

    print(imagine.split())
    # import re
    # l = re.split('[ ,]', imagine)
    # l.remove('')
    # print(l)
    print(imagine.split(', '))
    print(imagine.rsplit('.'))
    print()


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    # demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
