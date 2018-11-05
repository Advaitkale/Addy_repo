# Download the *.wav file to the python path before running the code

# It is a simple code of Speech Recognition using the google Speech Recognition API.
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("hello.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
