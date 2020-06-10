
#from wit import Wit #6.0.0
from chatters import Chatter
import talkers
import requests, json, time, sys
import speech_recognition as sr

API_ENDPOINT = "https://api.wit.ai/speech"
r = sr.Recognizer()
# TODO: make configurable in a more sensical way
r.pause_threshold = 0.2
r.non_speaking_duration = 0

# utility method for printing progress notices and stuff
def progress(*args,**kwargs):
    if(sys.stdout.isatty()):
        print("\033[2K\r", end='') # clear current line
        print(*args,**kwargs)    # pass args to print()
        print("\033[A", end='')  # UP
        sys.stdout.flush()

class WitChatter(Chatter):
    def __init__(self, auth_token, talker=talkers._instance):
        if type(auth_token) != str or len(auth_token) < 10:
            raise TypeError("invalid auth token")
        if type(talker) is talkers.Talker:
            raise TypeError("passed abstract Talker instance")
        if not(isinstance(talker, talkers.Talker)):
            raise TypeError("expected Talker subclass, was " + talker.__class__.__name__)
        #TODO: improve help to set up auth token
        self.auth_token = auth_token
        self.talker = talker
        self.source = sr.Microphone()

    def run(self, bot):
        try:
            while True:
                # record audio of specified length in specified audio file
                #with sr.Microphone() as source:
                progress("listening", time.strftime("%H:%M:%S"))
                with self.source as source:
                    audio = r.listen(source)
                progress("converting")
                wav_audio = audio.get_wav_data(
                            convert_rate=None if audio.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
                            convert_width=2  # audio samples should be 16-bit
                        )
                progress("recognizing via cloud")
                result = self.recognize_bytes(wav_audio)
                progress("")
                try:
                    text = result['text']
                    print(">",text)
                    response = bot.respond(result['text'])
                    print("*", response)
                    self.talker.say(response)
                except KeyError:
                    if 'entities' in result.keys() and result['entities'] == {}:
                        print("? noise ", len(wav_audio))
                        # TODO: figure out how to get actual duration
                    else:
                        print("# unknown response ", " ".join(result.keys()))
        except KeyboardInterrupt:
            pass # no op

    def recognize_bytes(self, audio):
        # defining headers for HTTP request
        headers = {'authorization': 'Bearer ' + self.auth_token,
                   'Content-Type': 'audio/wav'}

        # making an HTTP post request
        start = time.time()
        resp = requests.post(API_ENDPOINT, headers = headers,
                                         data = audio)
        duration = time.time() - start
        print("# %5.2f seconds to get response" % duration)
        # converting response content to JSON format
        data = json.loads(resp.content)
        return data

