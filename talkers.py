"""
Python module containing speech engines.
"""
import os


class Talker:
    """
    Abstract class representing all speech engines.

    The say() method should accept and discard unknown
    arguments, because I want to make configuration flexible.
    if logging is enabled I'll put up a warning for unknown
    options.
    """
    pass

    def say(self, sentence, *args, **kwargs):
        raise NotImplementedError("abstract Talker class")

class TextTalker(Talker):
    def say(self, sentence, *args, **kwargs):
        print(sentence)

defaultClass = TextTalker # should never be used



class MacOsTalker(Talker):
    def __init__(self):
        if os.uname().sysname != "Darwin":
            raise RuntimeError("created macOS talker while not running on MacOS")
    """
    Speech engine for the built-in ``say`` command in MacOS X.
    """
    def say(self, sentence, macvoice="Victoria", **kwargs):
        os.system("say -v %r %r" % (macvoice, sentence))

if os.uname().sysname == "Darwin":
    defaultClass = MacOsTalker

_instance = defaultClass()

def say(sentence, *args, **kwargs):
    """
    Say sentence using the default speech engine.
    Custom args will be passed along to any subclass.
    """
    _instance.say(sentence, *args, **kwargs)

if __name__ == "__main__":
    say("hello world", macvoice="Alex")
    say("goodbye world", "Alex")

