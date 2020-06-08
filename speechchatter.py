
from Recorder import record_audio, read_audio
#from wit import Wit #6.0.0
from chatters import Chatter
import talkers
import requests, json
import speech_recognition as sr
import time

# TODO: use non-deprecated endpoint
API_ENDPOINT = "https://api.wit.ai/speech"
r = sr.Recognizer()
r.pause_threshold = 0.1
r.non_speaking_duration = 0

class SpeechChatter(Chatter):
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

    def run(self, bot):
        try:
            while True:
                # record audio of specified length in specified audio file
                with sr.Microphone() as source:
                    audio = r.listen(source)
                wav_audio = audio.get_wav_data(
                            convert_rate=None if audio.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
                            convert_width=2  # audio samples should be 16-bit
                        )
                result = self.recognize_bytes(wav_audio)
                try:
                    text = result['text']
                    print(">",text)
                    response = bot.respond(result['text'])
                    print("*", response)
                    self.talker.say(response)
                except KeyError:
                    print("> ???", result.keys())
                    if '_text' in result.keys():
                        print(result["_text"])
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
        print(duration,"seconds to get response")
        # converting response content to JSON format
        data = json.loads(resp.content)
        return data

