"""Main module."""

# # Hello world: the print() built-in function and the + operator.
#
# print('Imagine')
# print('\'Imagine\' was released in 1971.')
# print('\'Imagine\' was released in ' + '1971.')
# print('\'Imagine\' was released in', '1971.')
# print('\'Imagine\' was released in', '\n1971.')


# The input() built-in function

# print('The year when "Imagine" was first released: ', end='')
# release_year = input()
# # print('Release year:', release_year)
# print('Release year: ' + release_year)

# release_year = int(input('The year when \'Imagine\' was first released: '))
# type(release_year)
# print('Release year: ' + str(release_year))


# A simple function and function call

# def release_year():
#     release_year = int(input('The year when \'Imagine\' was first released: '))
#     print('Release year: ' + str(release_year))
#     # return
#     return release_year
#
#
# # release_year()
# print(release_year())


# A simple loop and the range() built-in function

# for i in range(5):
#     print(i)
# print()
# i = 0
# while i < 5:
#     print(i)
#     i += 1


# A simple list, accessing list elements, printing lists

# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# print('The first Beatle:', theBeatles[0])
# print()
# print(theBeatles)

# Looping through list elements - for and enumerate()

# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# for beatle in theBeatles:
#     print(beatle)
# print()
# print('The Beatles:', ', '.join(beatle for beatle in theBeatles))
# print()
# for i, beatle in enumerate(theBeatles):
#     print(str(i+1) + ':', beatle)


# Global variables: __name__, __file__, __doc__,...

# print(__name__)
# print(__file__)
# print(__doc__)
# print(globals())

from python.inception import *
print(release_year())
