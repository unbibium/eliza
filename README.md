# unbibium's changes

With this fork, I'm trying to add some more ways to use Eliza as an object.

I've already added a way to change out the user interface without changing anything else.
I've added a rudimentary speech recognition interface that will just record five second
chunks and use wit.ai for speech-to-text.

```
$ python chat.py -h
```

It will only show audio options if the `WIT_AUTH_TOKEN` environment string is set with
the API key you got from wit.ai.
Currently it uses the "say" shell command in MacOS for speech.  If I ever need to run this on a Raspberry Pi, I'll add other options.

Next step is to add support for Snowboy wake words, so that it's possible to have a chatbot that sits around all day waiting for input.

I may be writing a chatbot later that responds to certain commands, and falls back to Eliza if nothing
is recognized.  At that point, I'll swap out the Eliza object with something else.

there will probably be a whole wrapper system but I'm getting ahead of myself.

Below is the original `README.md` from whence I forked.

# Eliza chatbot in Python

Loosely based on Charles Hayden's version in Java, at http://chayden.net/eliza/Eliza.html. 

I feel that it is fairly complete. However there are some holes, as the library was written immediately prior to my discovery of Joseph Weizenbaum's own description of the original program, which is quite detailed, along with the original "doctor" script. Oh well. A copy of that article is provided in the repo as a reference to the correct behavior.

