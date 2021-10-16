"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


# def demonstrate_annotations(musician, year=1940):
def demonstrate_annotations(musician, year):
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """


def show_musician(name, year=1940, city='Liverpool'):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """


def use_flexible_arg_list(band_name: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """


def use_all_categories_of_args(band, *members, year=1962, **music_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """


if __name__ == "__main__":

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # demonstrate_annotations(john)
    # demonstrate_annotations(musician, year=1957)

    # show_musician(john)

    # use_flexible_arg_list('The Beatles', *the_beatles)
    # use_flexible_arg_list('The Beatles')

    # use_all_categories_of_args('The Beatles', start=1962, end=1970)
    # use_all_categories_of_args('The Beatles', *the_beatles, start=1962, end=1970)


