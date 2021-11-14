"""The class representing the concept of playlist.
It includes a list of Song objects and the dates when the playlist was created and completed.
"""

from datetime import date, datetime, time
import json

from music.song import Song
from util.utility import format_date
from settings import PREFERRED_DATE_FORMAT


class Playlist:
    """The class representing the concept of playlist.
    It includes a list of Song objects and the dates when the playlist was created and completed.
    """

    # Class variables: much like static fields in Java; typically defined and initialized before __init__()
    # Insert one or more class variables (static fields), such as phrases used in __str__(), date_pattern,...

    play_me = 'Play me :)'

    def __init__(self, name, *songs, created=date.today(), completed=date.today()):
        self.name = name if isinstance(name, str) else 'unknown'
        self.songs = songs
        # self.songs = songs if all([isinstance(song, Song) for song in songs]) else None
        self.created = created if isinstance(created, date) else None
        self.completed = completed if isinstance(completed, date) else None
        # self.__i = 0

    def __str__(self):
        name = self.name.capitalize() + ' playlist:\n'
        songs = f'{"; ".join([str(song) for song in self.songs])}' + '\n' if self.songs else ''
        from_to = f'{format_date(self.created)} - {format_date(self.completed)}'
        return name + songs + from_to

    def __eq__(self, other):
        isi = isinstance(other, Playlist)
        n = self.name == other.name
        s = (len(self.songs) == len(other.songs)) and all([s in other.songs for s in self.songs])
        from_to = (self.created == other.created) and (self.completed == other.completed)
        return isi and n and s and from_to

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

        lines = playlist_str.split('\n') if isinstance(playlist_str, str) else []
        if len(lines) == 3:
            l1, l2, l3 = lines
        elif len(lines) == 2:
            l1, l3 = lines
            l2 = ''
        else:
            l1 = l2 = l3 = ''

        name = songs = created = completed = None
        if l1 and l3:
            name = l1.split(' playlist:')[0]
            created, completed = [datetime.strptime(d, PREFERRED_DATE_FORMAT).date() for d in l3.split(' - ')]
        if l2:
            songs = [Song.from_str(song_string) for song_string in l2.split('; ')]

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
            next_song = self.songs[self.__i]
            self.__i += 1
            return next_song
        else:
            raise StopIteration


def next_song(playlist):
    """Generator that shows the songs in a playlist, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for song in playlist:
        input('Next: ')
        yield song
        print('Yeah!')


class PlaylistEncoder(json.JSONEncoder):
    """JSON encoder for Playlist objects (cls= parameter in json.dumps()).
    """

    def default(self, playlist):
        # recommendation: always use double quotes with JSON

        pass


def playlist_py_to_json(playlist):
    """JSON encoder for Playlist objects (default= parameter in json.dumps()).
    """


def playlist_json_to_py(playlist_json):
    """JSON decoder for Playlist objects (object_hook= parameter in json.loads()).
    """


if __name__ == "__main__":

    from testdata.songs import *

    # # Class variables (like static fields in Java; typically defined and initialized before __init__())
    # print(Playlist.play_me)
    # print()

    # Check the basic methods (__init__(), __str__(),...)
    pl = Playlist('My favorite songs', *[imagine, love, across_the_universe, happiness_is_a_warm_gun],
                  created=date(2021, 11, 12))
    print(pl)
    print(pl == Playlist('My favorite songs', *[imagine, love, across_the_universe, happiness_is_a_warm_gun],
                         created=date(2021, 11, 12)))
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Playlist.is_date_valid(date.today()))
    print(Playlist.is_date_valid(date(2009, 3, 4)))
    print()

    # Check the alternative constructor (@classmethod from_playlist_str(<playlist_str>))
    pl_str = pl.__str__()
    pl1 = Playlist.from_playlist_str(pl_str)
    print(pl1)
    print()

    # Check the iterator
    # iter(pl)
    # for _ in range(len(pl.songs)):
    #     print(pl.__next__())
    # print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted

    # iter(pl)                          # without this reinitialization of the iterator, StopError is raised
    # print(pl.__next__())
    # for _ in range(len(pl.songs)):
    #     print(pl.__next__())
    # print()

    # i = iter(pl)
    # for _ in range(len(pl.songs)):
    #     print(next(i))
    # print()

    # # Demonstrate generators
    # song_generator = next_song(pl)
    # while True:
    #     try:
    #         print(next(song_generator))
    #     except StopIteration:
    #         break
    # print()

    # # Repeated attempt to run the generator fails, because the generator is exhausted
    # # print(next(song_generator))
    # song_generator = next_song(pl)
    # print(next(song_generator))

    # Demonstrate generator expressions
    # print(i**2 for i in range(3))
    # print(next(i**2 for i in range(3)))         # 0
    # print(next(i**2 for i in range(3)))         # 0 again, because the generator is created and initialized again
    g = (i**2 for i in range(3))
    print(g)
    print(next(g))                                # 0
    print(next(g))                                # 1
    print(next(g))                                # 4
    # print(next(g))                              # raises StopIteration, because the generator is exhausted
    print()


    # Demonstrate JSON encoding/decoding of Playlist objects
    # Single object
    print()

    # List of objects
    print()

    # def test():
    #     s = 'Imagine; Love (unplugged); Across the Universe; Happiness is a Warm Gun'
    #     print(s.split('; '))
    #     # print(pl_str)
    #     songs = [Song.from_str(song_string) for song_string in s.split('; ')]
    #     # for song in songs:
    #     #     print(song.title)
    #     s_split = s.split('; ')
    #     print(Song.from_str(s.split('; ')[3]))
    #
    # test()
