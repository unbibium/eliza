
from Recorder import record_audio, read_audio
#from wit import Wit #6.0.0
from chatters import Chatter
import requests, json

# TODO: use non-deprecated endpoint
API_ENDPOINT = "https://api.wit.ai/speech"

class SpeechChatter(Chatter):
    def __init__(self, auth_token):
        if type(auth_token) != str or len(auth_token) < 10:
            raise ValueError("invalid auth token")
        #TODO: improve help to set up auth token
        self.auth_token = auth_token

    def run(self, bot, num_seconds = 5):
        try:
            AUDIO_FILENAME="fff.wav"
            while True:
                # record audio of specified length in specified audio file
                record_audio(num_seconds, AUDIO_FILENAME)
                # reading audio
                audio= read_audio(AUDIO_FILENAME)
                result = self.recognize_bytes(audio)
                try:
                    text = result['text']
                    print(">",text)
                    response = bot.respond(result['text'])
                    print("*", response)
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
        resp = requests.post(API_ENDPOINT, headers = headers,
                                         data = audio)
                                             
        # converting response content to JSON format
        data = json.loads(resp.content)
        return data

    def recognize(self, audio_data):
        """
        Performs speech recognition on ``audio_data`` (an ``AudioData`` instance),
        using the Wit.ai API and the key given in the constructor.

        """
        #assert isinstance(audio_data, AudioData), "Data must be audio data"

        wav_data = audio_data.get_wav_data(
            convert_rate=None if audio_data.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
            convert_width=2  # audio samples should be 16-bit
            )
        return self.api.speech(audio_data)

    def reply(self, text):
        # TODO: make it say stuff aloud
        print("... \033[1m", text, "\033[0m")
