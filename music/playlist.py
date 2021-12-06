"""The class representing the concept of playlist.
It includes a list of Song objects and the dates when the playlist was created and completed.
"""
import pickle
from datetime import date, datetime, time
from pathlib import Path
import sys
from pickle import *
import json

from music.song import Song, song_py_to_json, song_json_to_py
# from util.utility import format_date
# from settings import PREFERRED_DATE_FORMAT
from settings import *
from util.utility import *


class Playlist:
    """The class representing the concept of playlist.
    It includes a list of Song objects and the dates when the playlist was created and completed.
    """

    # Class variables: much like static fields in Java; typically defined and initialized before __init__()
    # Insert one or more class variables (static fields), such as phrases used in __str__(), date_pattern,...

    play_me = 'Play me :)'

    def __init__(self, name, *songs, created=date.today(), completed=date.today()):
        if created > completed:
            raise PlaylistDateError(created, completed)
        self.name = name
        self.songs = songs
        self.created = created
        self.completed = completed
        # pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        n = self.name
        s = '; '.join([str(song) for song in self.songs]) if self.songs else '(empty)'
        from_to = date.strftime(self.created, PREFERRED_DATE_FORMAT) + ' - ' + \
                  date.strftime(self.completed, PREFERRED_DATE_FORMAT)
        return '\n'.join([n, s, from_to])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ if type(self) is type(other) else False

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a playlist has not been created more than ~10 years ago.
        So, the valid date to denote the creation of a playlist is between Jan 01, 2011, and today.
        """

        return date(2011, 1, 1) <= d <= date.today()

    @staticmethod
    def parse_playlist_str(playlist_str):
        """Splits a playlist string into its typical segments.
        """

        l1, l2, l3 = playlist_str.split('\n')
        name = l1
        songs = [Song.from_str(s) for s in l2.split('; ')] if l2 != '(empty)' else []
        created, completed = [datetime.strptime(d, PREFERRED_DATE_FORMAT).date() for d in l3.split(' - ')]
        return name, songs, created, completed

    # Alternative constructor
    @classmethod
    def from_playlist_str(cls, playlist_str):
        name, songs, created, completed = Playlist.parse_playlist_str(playlist_str)
        return cls(name, *songs, created=created, completed=completed)

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized  here.
        """

        # return self               # sufficient if the iterator counter is introduced and initialized in __init__()
        self.__i = 0
        return self

    def __next__(self):
        if self.__i < len(self.songs):
            s = self.songs[self.__i]
            self.__i += 1
            return s
        else:
            raise StopIteration


def next_song(playlist):
    """Generator that shows the songs in a playlist, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for s in playlist.songs:
        input('Next:')
        yield s
        print('Yeah!')


class PlaylistError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class PlaylistDateError(PlaylistError):
    """Exception raised when the date when a playlist was created is after the date when the playlist was completed.
    """

    # define __init__() to include an appropriate message if the input args (created, completed) dates are not OK
    def __init__(self, created, completed):
        self.message = f'date created ({created}) after date completed ({completed})\n\n'


class PlaylistEncoder(json.JSONEncoder):
    """JSON encoder for Playlist objects (cls= parameter in json.dumps()).
    """

    def default(self, playlist):
        # recommendation: always use double quotes with JSON

        pass


def playlist_py_to_json(playlist):
    """JSON encoder for Playlist objects (default= parameter in json.dumps()).
    """

    if isinstance(playlist, Playlist):
        d = playlist.__dict__.copy()
        d["songs"] = json.dumps(playlist.songs, default=song_py_to_json)
        d["created"] = date_py_to_json(playlist.created)
        d["completed"] = date_py_to_json(playlist.completed)
        return {"__Playlist__": d}
    raise TypeError('not a Playlist object')


def playlist_json_to_py(playlist_json):
    """JSON decoder for Playlist objects (object_hook= parameter in json.loads()).
    """

    # The songs field is specified as *songs in Playlist.__init__(),
    # make sure to use tuple(json.loads(<songs in playlist_json>))

    if "__Playlist__" in playlist_json:
        p = Playlist('')
        d = playlist_json["__Playlist__"]
        p.songs = tuple(json.loads(d["songs"], object_hook=song_json_to_py))
        p.created = date_json_to_py(d["created"])
        p.completed = date_json_to_py(d["completed"])
        return p
    return playlist_json


if __name__ == "__main__":

    from testdata.songs import *

    # Class variables (like static fields in Java; typically defined and initialized before __init__())
    print(Playlist.play_me)
    print()

    # Check the basic methods (__init__(), __str__(),...)
    pl = Playlist('My songs', *[across_the_universe, imagine, happiness_is_a_warm_gun, love],
                  created=date(2019, 2, 4), completed=date.today())
    print(pl)
    print(pl == Playlist('My songs', *[across_the_universe, imagine, happiness_is_a_warm_gun, love],
                         created=date(2019, 2, 4), completed=date.today()))
    print()
    print(Playlist('My songs', created=date(2019, 2, 4), completed=date.today()))
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Playlist.is_date_valid(date(2014, 3, 6)))
    print()

    # Check the alternative constructor (@classmethod from_playlist_str(<playlist_str>))
    pls = pl.__str__()
    print(Playlist.from_playlist_str(pls))
    print(pl == Playlist.from_playlist_str(pls))
    print()

    # Check the iterator
    i = iter(pl)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    i = iter(pl)
    print(next(i))
    print()

    # # Demonstrate generators
    # next_s = next_song(pl)
    # while True:
    #     try:
    #         print(next(next_s))
    #     except StopIteration:
    #         break
    # print()
    #
    # # Repeated attempt to run the generator fails, because the generator is exhausted
    # print()

    # # Demonstrate generator expressions
    # e = (i**2 for i in [1, 2, 3])
    # print(e)
    # print(next(e))
    # print(next(e))
    # print()

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    songs = [love, happiness_is_a_warm_gun, across_the_universe, imagine]
    # # print(3 / 0)
    # # print(songs[4])
    # try:
    #     # print(3/0)
    #     print(songs[6])
    # except ZeroDivisionError:
    #     # print('Zero division')
    #     sys.stderr.write('Zero division')
    # except IndexError as e:
    #     # sys.stderr.write(str(e.args))
    #     sys.stderr.write(e.args[0])
    # else:
    #     print('Nothing irregular happened')
    # finally:
    #     print('And this runs regardless...')
    print()

    # Demonstrate exceptions - except: Exception as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    print()

    # # Demonstrate exceptions - user-defined exceptions (wrong playlist date(s))
    # p = Playlist('My playlist')
    # try:
    #     p = Playlist('My playlist', *songs, created=date(2022, 2, 3), completed=date.today())
    #     print(p)
    # except PlaylistDateError as e:
    #     sys.stderr.write(e.__class__.__name__ + ': ' + e.message)
    #     raise
    # print()

    # # Demonstrate writing to a text file - <outfile>.write(), <outfile>.writelines()
    # file = get_data_dir() / 'songs.txt'
    # with open(file, 'w') as f:
    #     # for s in songs:
    #     #     f.write(str(s) + '\n')
    #     f.writelines([str(s) + '\n' for s in songs])
    # print('Done')
    # print()

    # # Demonstrate reading from a text file - <infile>.read(), <infile>.readline()
    # file = get_data_dir() / 'songs.txt'
    # with open(file, 'r') as f:
    #     # # for s in songs:
    #     # #     f.write(str(s) + '\n')
    #     # lines = f.read().rstrip()
    #     lines = ''
    #     while True:
    #         line = f.readline()
    #         if line:
    #             lines = lines + line
    #         else:
    #             break
    # # print(lines)
    # songs1 = [Song.from_str(line) for line in lines.split('\n')]
    # print('; '.join([str(s) for s in songs1]))
    # print('Done')
    # print()

    # Demonstrate writing to a binary file - pickle.dump()
    # file = get_data_dir() / 'songs.binary'
    # with open(file, 'wb') as f:
    #     pickle.dump(songs, f)
    # print('Done')
    print()

    # # Demonstrate reading from a binary file - pickle.load()
    # file = get_data_dir() / 'songs.binary'
    # with open(file, 'rb') as f:
    #     songs1 = pickle.load(f)
    # print('Done')
    # print('; '.join([str(s) for s in songs1]))
    print()

    # Demonstrate JSON encoding/decoding of Playlist objects
    # Single object
    pl_json = json.dumps(pl, default=playlist_py_to_json, indent=4)
    print(pl_json)
    pl_py = json.loads(pl_json, object_hook=playlist_json_to_py)
    print(pl_py)
    print()

    # List of objects
    pll_json = json.dumps([pl, pl], default=playlist_py_to_json, indent=4)
    pll_py = json.loads(pll_json, object_hook=playlist_json_to_py)
    for p in pll_py:
        print(p)
    print()


