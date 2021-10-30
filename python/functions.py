"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


def demonstrate_annotations(song: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(song, year)
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__name__)
    print(demonstrate_annotations.__doc__)
    return f'This is the result of calling {demonstrate_annotations.__name__}(\'{song}\', {year}).'


# def show_song(title, author='John Lennon', year: int = 1971):
def show_song(title, author='John Lennon', year=1971):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())
    print(f'{title}, by {author} (year)')


def use_flexible_arg_list(band_name: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # print(type(members))
    # print(band_name + ':', ', '.join(members))
    print(band_name + ': ' + ', '.join(members) if members else band_name)


def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    # print(type(details))
    # print(details)
    # print(locals())

    active = 'active' if is_active else 'not active'
    main = f'{band} ({active}): {", ".join(members)}' if members else f'{band} ({active})'
    # rest = f'({[str(k) + ": " + str(v) for k, v in details.items()]})' if details else ''
    rest_list = [str(k) + ": " + str(v) for k, v in details.items()]
    rest = f'({", ".join(rest_list)})' if details else ''
    print(main, rest)


if __name__ == "__main__":

    imagine = 'Imagine'
    year = 1971

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # print(demonstrate_annotations(imagine, year))

    # show_song(imagine)

    # use_flexible_arg_list('The Beatles', *the_beatles)
    # use_flexible_arg_list('The Beatles', *[john, paul, george, ringo])
    # use_flexible_arg_list('The Beatles', john, paul, george, ringo)
    # use_flexible_arg_list('The Beatles')

    use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
    use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970)


