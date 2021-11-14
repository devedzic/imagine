"""The class representing the concept of playlist.
It includes a list of Song objects and the dates when the playlist was created and completed.
"""

from datetime import date, datetime, time
import json

# from music.song import Song
# from util.utility import format_date


class Playlist:
    """The class representing the concept of playlist.
    It includes a list of Song objects and the dates when the playlist was created and completed.
    """

    # Class variables: much like static fields in Java; typically defined and initialized before __init__()
    # Insert one or more class variables (static fields), such as phrases used in __str__(), date_pattern,...

    def __init__(self, name, *songs, created=date.today(), completed=date.today()):
        pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a playlist has not been created more than ~10 years ago.
        So, the valid date to denote the creation of a playlist is between Jan 01, 2011, and today.
        """
        pass

    @staticmethod
    def parse_playlist_str(self, playlist_str):
        """Splits a playlist string into its typical segments.
        """
        pass

    # Alternative constructor
    @classmethod
    def from_playlist_str(cls, playlist_str):
        pass

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized  here.
        """

        pass
        # return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        pass


def next_song(playlist):
    """Generator that shows the songs from a playlist, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """


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

    # from testdata.songs import *

    # Class variables (like static fields in Java; typically defined and initialized before __init__())
    print()

    # Check the basic methods (__init__(), __str__(),...)
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print()

    # Check the alternative constructor (@classmethod from_playlist_str(<playlist_str>))
    print()

    # Check the iterator
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted

    # Demonstrate generators
    print()

    # Repeated attempt to run the generator fails, because the generator is exhausted
    print()

    # Demonstrate generator expressions
    print()

    # Demonstrate JSON encoding/decoding of Playlist objects
    # Single object
    print()

    # List of objects
    print()


