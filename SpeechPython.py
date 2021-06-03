# -----------------------------------------------------------------------------
# DISCLAIMER: googletrans 3.0.0 is an unofficial library using the web API of 
# translate.google.com and also is not associated with Google.
# # The maximum character limit on a single text is 15k.
# Due to limitations of the web version of google translate, this API does not 
# guarantee that the library would work properly at all times 
# (so please use this library if you don’t care about stability).

# Important: If you want to use a stable API, I highly recommend you to use Google’s official translate API.
# If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.

# Python play to look up and a term on wikipedia using speech recognition. 
# The first sentence is retrieved and saved as an audiofile and played.
# several modules were installed to get this to work. 
# ie. 
#   pip install wikipedia
#   pip install speech_recognition ?
#   pip install SpeechRecognition
#   pip install pygame
#
#   pip install googletrans (working on this later)
#   
# https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvprop=content&titles=Two_Publics
#
# -----------------------------------------------------------------------------
import typing

import wikipedia
import json
import re
import speech_recognition as sr
from gtts import gTTS
import time
from pygame import mixer
#quiet the endless 'insecurerequest' warning
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from googletrans import Translator

staticVal:int = 0

mixer.init()

doVR = True

while (True == doVR ):

    dictation = ""
    sentences1 = ""
    staticVal += 1
    # Record Audio
    r = sr.Recognizer()
    print("Say something!")

    with sr.Microphone() as source:
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, 
        # use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        dictation = r.recognize_google(audio)
        print("You said: " + dictation)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    # trigger words
    regex = r"(exit please)"
    if re.search(regex, dictation) or len(dictation) == 0:
        break

    else:
        # someval = wikipedia.page(dictation)
        # links = []
        # links = someval.links
        # print("number of links ", len(links))

        sentences1 = wikipedia.summary(dictation, sentences=1)
        if len(sentences1) == 0:
            continue

        tts = gTTS(text=str(sentences1), lang='en')
        epoch_time = int(time.time())
        laSentenceDuFile = "speech_wikisearch_" + str(epoch_time) + ".mp3"
        tts.save(laSentenceDuFile)

        mixer.music.load(laSentenceDuFile)
        mixer.music.play()


    print("end of search number : " + str(staticVal))

print("... done")

#do more with this later
japanWorws = "안녕하세요"
translator = Translator()
translations = translator.translate(japanWorws)
print (" translates to " + translations.text )