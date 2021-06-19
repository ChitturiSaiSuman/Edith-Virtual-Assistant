""" This program plays the music and videos from youtube """

import speech_recognition as sr
import webbrowser
import urllib.request
import urllib.parse
import re
from sys import argv

# get audio from microphone
#r = sr.Recognizer()
#with sr.Microphone() as source:                                                                       
#    print("which song you wanna listen:")                                                                                   
#    audio = r.listen(source)

# get the text from audio
#msg = r.recognize_google(audio)

msg = argv[1]

# song name from user
song = urllib.parse.urlencode({"search_query" : msg})
#print(song)

# fetch the ?v=query_string
result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
#print(result)

# make the url of the first result song
#print(result.read().decode())
search_results = re.findall(r'\/watch\?v=(.{11})', result.read().decode())
#print(search_results)

# make the final url of song selects the very first result from youtube result
url = "http://www.youtube.com/watch?v="+search_results[0]

# play the song using webBrowser module which opens the browser 
# webbrowser.open(url, new = 1)
webbrowser.open_new(url)
