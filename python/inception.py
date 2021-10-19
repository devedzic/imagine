"""The very first module in a more structured version of the project.
"""


# Moving code from main.py

def release_year():
    """A simple function defined in a module.
    """
    release_year = int(input('The year when \'Imagine\' was first released: '))
    print('Release year: ' + str(release_year))
    # return
    return release_year


# release_year()
# print(release_year())


# Taking care of the module __name__

if __name__ == '__main__':

    # print('Imagine')
    # print('\'Imagine\' was released in 1971.')
    # print('\'Imagine\' was released in ' + '1971.')
    # print()
    # print(release_year())


    # Printing with ' ' and printing without '\n'

    # print('The year when "Imagine" was first released:', end=' ')
    # release_year = input()
    # # print('Release year:', release_year)
    # print('Release year: ' + release_year)


    # Printing with classical formatting (%)

    # # print('The song %s was first released in %d.' % ('Imagine', 1971))
    # year = 1971
    # # print(type(year), year)
    # song = 'Imagine'
    # print(f'The song {song} was first released in {year}.')


    # Keyboard input

    # release_year = int(input('The year when \'Imagine\' was first released: '))
    # type(release_year)
    # print('Release year: ' + str(release_year))


    # break and continue

    # for i in range(2, 15, 2):
    #     if i == 6:
    #         # continue
    #         break
    #     print(i)


    # Printing docstrings

    # print(__doc__)
    # print(release_year.__doc__)


    # Printing a list using enumerate()

    # theBeatles = ['John', 'Paul', 'George', 'Ringo']
    # print(theBeatles)
    # print(enumerate(theBeatles))
    # print(list(enumerate(theBeatles)))

    # Importing from Standard Library

    from datetime import date
    theDate = date(1971, 10, 11)
    print(theDate)
    date_formatting_string = '%b %d, %Y'
    print(theDate.strftime(date_formatting_string))
