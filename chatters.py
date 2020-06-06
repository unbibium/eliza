#!/usr/bin/env python3

pass
class Chatter:
    """
    Abstract class for user interfaces to interface with chat.
    """
    pass

class ScriptChatter(Chatter):
    def __init__(self, path):
        self.path = path

    def run(self, bot):
        if(hasattr(bot, "initial")):
            print("*", bot.initial())
        try:
            with open(self.path) as f:
                for line in f.readlines():
                    print(">", line.rstrip())
                    print("*", bot.respond(line.rstrip()))
        except KeyboardInterrupt:
            print("^C")
            pass # no op, assume just broke out of loop
        if(hasattr(bot, "final")):
            print("*", bot.final())


class TextChatter(Chatter):
    def run(self, bot):
        if(hasattr(bot, "initial")):
            print("*", bot.initial())
        try:
            while True:
                line = input("> ") 
                print("*", bot.respond(line))
        except KeyboardInterrupt:
            print("^C")
            pass # no op, assume just broke out of loop
        if(hasattr(bot, "final")):
            print("*", bot.final())
        
