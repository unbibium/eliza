#!/usr/bin/env python3

from chatters import *
from eliza import *

if __name__ == "__main__":
    import sys, os, argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", action='store_true',
        help="Chat with terminal")
    parser.add_argument("-s", "--script", 
        help="Read input from SCRIPT and display to terminal")
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
        ux = AudioChatter()
    else:
        parser.print_help()
        sys.exit(2)
    ux.run(bot)

