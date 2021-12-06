"""Domain classes and functions related to the concept of song.
"""


# from util import utility
from music.enums import *
import json


class Song:
    """The class describing the concept of song.
    It is assumed that a song is sufficiently described by its
    title and whether it is "unplugged" song or not.

    This class illustrates some of the important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - __dict__ attribute of all objects
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """

    def __init__(self, title, is_unplugged=False):
        self.title = title
        self.is_unplugged = is_unplugged
        # self.__n = 'kkk'                                    # 'private' field
        # self._n = 'lll'                                     # 'protected' field

    # Properties: 'private' fields:
    #   @property
    #   def <attr>(self):
    #       return self.__<attr>
    #   @<attr>.setter
    #   def <attr>(self, <attr>):
    #       self.__<attr> = <attr> if ... else ...
    # Run setters and getters in the debugger.
    # Make title a property (after setting up __init__(), __str__(), __eq__(), methods,...).

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    # Add an immutable property (no setter for it) - just return self; prints as __str__().

    def __str__(self):
        return self.title + ' (unplugged)' if self.is_unplugged else self.title

    def __eq__(self, other):
        isi = isinstance(other, Song)
        t = self.title == other.title
        u = self.is_unplugged == other.is_unplugged
        return isi and t and u

    def play(self, artist, *args, **kwargs):
        """Assumes that artist, *args (e.g. expressions of gratitude) and kwargs.values() (e.g. messages) are strings.
        Prints song title, artist, and things like rhythm counts, expressions of gratitude and messages. A call example:
            <song>.play(artist, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        print(self.title)
        print(artist)
        if args:
            print(f'{", ".join([str(arg) for arg in args])}')
        if kwargs:
            print(f'{", ".join([str(k) + ": " + str(v) for k, v in kwargs.items()])}')

    def play_song(self, artist, *args, **kwargs):
        """Demonstrates calling another method from the same class (self.<method>(...) as a mandatory syntax).
        """
        self.play(artist, *args, **kwargs)

    # Alternative constructor
    @classmethod
    def from_str(cls, song_string):
        """Inverted __str__() method.
        Assumes that song_string is in the format generated by __str__().
        """

        # return self.title + ' (unplugged)' if self.is_unplugged else self.title
        t = song_string.split(' (unplugged)')[0]
        u = True if song_string.endswith(' (unplugged)') else False
        return cls(t, u)


class SongEncoder(json.JSONEncoder):
    """JSON encoder for Song objects (cls= parameter in json.dumps()).
    """

    def default(self, song):
        # recommendation: always use double quotes with JSON

        # can simply return song_py_to_json(song), to avoid code duplication
        return song_py_to_json(song)


def song_py_to_json(song):
    """JSON encoder for Song objects (default= parameter in json.dumps()).
    """

    # recommendation: always use double quotes with JSON
    if isinstance(song, Song):
        return {"__Song__": song.__dict__}
    raise TypeError('expected Song object')


def song_json_to_py(song_json):
    """JSON decoder for Song objects (object_hook= parameter in json.loads()).

    It is essential to run this code in the debugger. If the breakpoint is set at the very first line (the if statement)
    it is possible to see that, internally, this function runs TWICE per call (!!!) -
    the first time the if statement evaluates to False because the first time song_json does not include "__Song__" (!),
    and the return song_json actually does not return to the calling point but to some idiosyncratic Python functions
    that do some internal witchcraft; when they are done, this function resurrects at the if statement again and
    suddenly song_json DOES include "__Song__" and everything works fine (!?!?!).
    """

    if "__Song__" in song_json:
        s = Song('')
        s.__dict__.update(song_json["__Song__"])
        return s
    return song_json


class Ballad(Song):
    """The class describing the concept of ballad.
    It is assumed that a ballade is sufficiently described as a Song,
    with the addition of whether its tempo is slow or moderate.

    Useful link (related to inheritance in Python):
    https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs/3394902#3394902 (calling super() in constructors)
    """

    # # Version 1 - no multiple inheritance
    # def __init__(self, title, is_unplugged=False, tempo=Tempo.SLOW):
    #     super().__init__(title, is_unplugged)
    #     self.tempo = tempo

    # Version 2 - with multiple inheritance
    def __init__(self, tempo=Tempo.SLOW, **kwargs):
        super().__init__(**kwargs)
        self.tempo = tempo

    def __str__(self):
        return super().__str__() + '; ballad'

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if type(self) is type(other) else False

    def play(self, artist, *args, **kwargs):
        """Assumes that artist, *args (e.g. expressions of gratitude) and kwargs.values() (e.g. messages) are strings.
        Prints song title, artist, and things like rhythm counts, expressions of gratitude and messages. A call example:
            <song>.play(artist, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        super().play(artist, *args, **kwargs)
        print('ballad')


class PianoSong(Song):
    """The class describing the concept of piano song.
    It is assumed that a piano song is sufficiently described as a song
    in which the dominating instrument is piano.
    """

    # # Version 1 - no multiple inheritance
    # def __init__(self, title, is_unplugged=False, instrument=Instrument.PIANO):
    #     super().__init__(title, is_unplugged)
    #     self.instrument = instrument

    # Version 2 - with multiple inheritance
    def __init__(self, instrument=Instrument.PIANO, **kwargs):
        super().__init__(**kwargs)
        self.instrument = instrument

    def __str__(self):
        return super().__str__() + '; piano song'

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if type(self) is type(other) else False

    def details(self):
        """Just a simple method to indicate details of a piano song.
        """

        print(f'{self.title} is a nice {self.instrument.name.lower()} song :)')


class PianoBallad(Ballad, PianoSong):
# class PianoBallad(PianoSong, Ballad, ):
    """The class describing the concept of piano ballade.
    It is assumed that a piano ballade is sufficiently described as a song that is simultaneously piano-dominated.

    Useful links :
    https://stackoverflow.com/a/50465583/1899061 (designing classes (i.e. their __init__() methods) for multiple inh.)
    https://stackoverflow.com/a/533675/1899061 (mixins explained, and what good they are in multiple inheritance)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if type(self) is type(other) else False


if __name__ == "__main__":

    # from testdata.songs import *

    # Print objects
    imagine = Song('Imagine', is_unplugged=True)
    # imagine = Song('Imagine')
    print(imagine)
    print()

    # Compare objects
    print(imagine == Song('Imagine', is_unplugged=True))
    print(imagine == Song('Imagine'))
    print()

    # Access data fields (instance variables), including 'private' fields
    print(imagine.title)
    imagine.title = 'Imagine'
    print()
    # print(imagine.__n)
    # print(imagine._Song__n)
    # print(imagine._n)
    # print()

    # Add new data fields (instance variables)
    #   1. <object>.<new_attr> = <value>
    #   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
    #   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')
    imagine.year = 1971
    print(imagine.year)
    print()

    # Calling methods
    imagine.play('John Lennon', *[1971, 'Oct 11'], rec_from='May 1971', rec_to='July 1971')
    imagine.play('John Lennon', rec_from='May 1971', rec_to='July 1971')
    print()
    imagine.play_song('John Lennon', *[1971, 'Oct 11'], rec_from='May 1971', rec_to='July 1971')
    print()

    # Demonstrate object data fields and methods in Python Console for some built-in classes (boolean, int, object,...)
    # - True + 1
    # - True.__int__()
    # - (1).__class__.__name__
    # - (1).__class__
    # - o.__dir__()
    # - o.__dir__
    # - o.__dict__

    # Demonstrate object data fields and methods for Musician objects
    print(imagine.__dir__())
    print(imagine.__dict__)
    print(imagine.__class__.__name__)
    print()

    # Demonstrate @classmethod (from_str())
    print(imagine.from_str(imagine.__str__()))
    print(Song.from_str(imagine.__str__()))
    print()

    # Demonstrate inheritance
    # object class
    #   it's like the Object class in Java
    #   all classes inherit from object - try, e.g., list.__mro__ in the console
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented
    patience = Ballad(title='Patience', is_unplugged=True, tempo=Tempo.SLOW)
    print(patience)
    print(patience == Ballad(title='Patience', is_unplugged=True, tempo=Tempo.SLOW))
    print()
    let_it_be = PianoSong(title='Let It Be', )
    print(let_it_be)
    print(let_it_be == PianoSong(title='Let It Be', ))
    let_it_be.details()
    print()

    # Demonstrate method overriding
    patience.play('Guns & Roses', *['Axel Rose', 'Slash'], hit=True)
    print()

    # Demonstrate multiple inheritance and MRO.
    # Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).
    hey_jude = PianoBallad(title='Hey Jude', is_unplugged=False, instrument=Instrument.PIANO, tempo=Tempo.MODERATE)
    print(hey_jude)
    print(hey_jude == PianoBallad(title='Hey Jude', is_unplugged=False, instrument=Instrument.PIANO, tempo=Tempo.MODERATE))
    print(PianoBallad.__mro__)
    print()

    # Demonstrate JSON encoding/decoding of simple data types.
    # Refer to https://docs.python.org/3.3/library/json.html#encoders-and-decoders for details.
    print()

    # Demonstrate JSON encoding/decoding of Song objects
    # Single object
    imagine_json = json.dumps(imagine, cls=SongEncoder, indent=4)
    # imagine_json = json.dumps(imagine, default=song_py_to_json, indent=4)
    print(imagine_json)
    print()
    imagine_py = json.loads(imagine_json, object_hook=song_json_to_py)
    print(imagine_py)
    print()

    # # Try an object of different type
    # hey_jude_json = json.dumps(hey_jude, default=song_py_to_json, indent=4)

    # List of objects

    print()

