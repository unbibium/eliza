#!/usr/bin/env python3

from chatters import TextChatter, ScriptChatter
from speechchatter import SpeechChatter
from eliza import Eliza

if __name__ == "__main__":
    import sys, os, argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", action='store_true',
        help="Chat with terminal")
    parser.add_argument("-s", "--script", 
        help="Read input from SCRIPT and display to terminal")
    parser.add_argument("-a", "--audio", action='store_true',
        help="Chat with mic and speaker")
    parser.add_argument("-m", "--memory", 
        help="Saved memory file to use for Eliza")
    args = parser.parse_args()
    if args.memory:
        bot = Eliza(args.memory)
    else:
        bot = Eliza()
    bot.load("doctor.txt")
    ux = None
    if args.script:
        if not os.path.exists(args.script):
            print("error: file not found:", args.script)
            sys.exit(2)
        ux = ScriptChatter(args.script)
    elif args.terminal:
        ux = TextChatter()
    elif args.audio:
        auth_token = (os.environ.get('WIT_AUTH_TOKEN'))
        if type(auth_token) != str or len(auth_token) < 10:
            print("error: set environment string WIT_AUTH_TOKEN to a valid thingy")
            sys.exit(3)
        ux = SpeechChatter(auth_token)
    else:
        parser.print_help()
        sys.exit(2)
    ux.run(bot)

