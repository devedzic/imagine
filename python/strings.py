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

    print('%s was first released in %d. It has been sold in %1.2f million copies %s.' % ('Imagine', 1971, 20.2, 'worldwide'))
    print()

    print('C:\none')
    print(r'C:\none')
    print('      Imagine' * 3)
    print()

    print('Imagine'[:3])
    print('Imagine'[:-3])
    print('Imagine'[-3:])
    print('Imagine'[:])
    print()

    print(str('Imagine   '))
    print(repr('Imagine   '))
    print(repr('Imagine   \t'))
    print(repr('Imagine   ' + '\t'))
    print()


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{} was first released in {}. It is a song written and performed by {}.'.format('Imagine', 1971, 'John Lennon'))
    print()


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    song = 'Imagine'
    author = 'John Lennon'
    print(f'{song} was first released in {1971}. It is a song written and performed by {author}.')
    print()


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    imagine = 'Imagine was first released in 1971. It is a song written and performed by John Lennon.'

    print(imagine.endswith('Lennon.'))
    print(imagine.split())
    print(imagine.split('Imagine was '))
    print('Imagine'.center(30, '*'))
    print('mag' in 'Imagine')
    print('Imagine' == 'Imagine')
    print(len('Imagine'))
    print('  Imagine     ')
    print('  Imagine     '.lstrip())
    print()


if __name__ == '__main__':

    demonstrate_formatting()
    demonstrate_fancy_formatting()
    demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
