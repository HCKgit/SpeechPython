# https://www.geeksforgeeks.org/convert-text-speech-python/
# https://readthedocs.org/projects/gtts/downloads/pdf/latest/
# also to try https://deepspeech.readthedocs.io/en/r0.9/USING.html
# also to try https://www.raspberrypi.org/forums/viewtopic.php?t=275910
# aside: https://www.linode.com/docs/guides/visualize-apache-web-server-logs-using-elastic-stack-on-debian-10/


# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'I just called, to say, I love you.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=True)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("love_call.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")
