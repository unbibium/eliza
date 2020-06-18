#!/usr/bin/env python3

from chatters import TextChatter, ScriptChatter
from witchatter import WitChatter
from eliza import Eliza

if __name__ == "__main__":
    import sys, os, argparse
    wit_auth_token = os.getenv('WIT_AUTH_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", action='store_true',
        help="Chat with terminal")
    parser.add_argument("-s", "--script", 
        help="Read input from SCRIPT and display to terminal")
    if wit_auth_token:
        parser.add_argument("-a", "--audio", action='store_true',
            help="Chat with mic and speaker")
        parser.add_argument("-l", "--list-microphones", action='store_true',
            help="List microphone numbers and names and exit.")
        # TODO support --mic name
        parser.add_argument("-m", "--mic", "--microphone",
            help="Use microphone with given number")
    parser.add_argument("-M", "--memory", 
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
        micIndex = None
        if args.mic is not None:
            try:
                micIndex = int(args.mic)
            except ValueError:
                from speech_recognition import Microphone
                try:
                    micIndex = Microphone.list_microphone_names().index(args.mic)
                except ValueError:
                    print("cannot find mic named", args.mic)
                    sys.exit(4)
        ux = WitChatter(wit_auth_token, mic=micIndex)
    elif args.list_microphones:
        from speech_recognition import Microphone
        for i, name in enumerate(Microphone.list_microphone_names()):
            print(i,":", name)
            sys.exit(0)
    else:
        parser.print_help()
        sys.exit(2)
    ux.run(bot)

