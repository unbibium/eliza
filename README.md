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

Next step is to streamline speech recognition by making it listen passively and only react
when there is speech, and record for as long as speech is detected.  I may also use Snowboy 
to create a wake word, and make this work with that... 

I may be writing a chatbot later that responds to certain commands, and falls back to Eliza if nothing
is recognized.  At that point, I'll swap out the Eliza object with something else.

there will probably be a whole wrapper system but I'm getting ahead of myself.

# original Eliza chatbot in Python

Loosely based on Charles Hayden's version in Java, at http://chayden.net/eliza/Eliza.html. 

I feel that it is fairly complete. However there are some holes, as the library was written immediately prior to my discovery of Joseph Weizenbaum's own description of the original program, which is quite detailed, along with the original "doctor" script. Oh well. A copy of that article is provided in the repo as a reference to the correct behavior.

