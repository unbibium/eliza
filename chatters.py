#!/usr/bin/env python3

class Chatter:
    """
    Abstract class for user interfaces to interface with chat.

    Subclasses must define __iter__() and say()
    """
    def run(self, bot):
        if(hasattr(bot, "initial")):
            self.say(bot.initial())
        for line in self:
            self.say(bot.respond(line))
        if(hasattr(bot, "final")):
            self.say(bot.final())

class TextChatter(Chatter):
    """
    Reads input from the terminal, and writes responses to the terminal.
    """
    def __iter__(self):
        try:
            while True:
                yield(input("> "))
        except KeyboardInterrupt:
            print("^C")
        except EOFError:
            pass

    def say(self, response):
        print("*", response)

class ScriptChatter(TextChatter):
    """
    Reads input from a file, and writes responses to the terminal.
    """
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f.readlines():
                print(">", line.rstrip())
                yield(line.rstrip())

