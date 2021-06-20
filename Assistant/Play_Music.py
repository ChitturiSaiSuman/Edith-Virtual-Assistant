# This program plays the music and videos from youtube

import os               # For system calls
import signal           # For SIGTERM value
import pafy             # Used to collect duration of video
import re               # Used to parse the webpage of search results
import urllib.request   # To create a request to URL
import urllib.parse     # To encode URLs
import subprocess       # To Play song on Chrome
import time             # For sleep

def write_to_file(msg):
    with open("buffer.txt", "w") as file:
        file.write(msg)

def play_song(msg):

    # song name from user
    song = urllib.parse.urlencode({"search_query" : msg})

    # fetch the ?v=query_string
    result = urllib.request.urlopen("http://www.youtube.com/results?" + song)

    # make the url of the first result song
    search_results = re.findall(r'\/watch\?v=(.{11})', result.read().decode())

    # make the final url of song; selects the very first result from youtube result
    url = "https://www.youtube.com/watch?v=" + search_results[0]

    # Extract the length of video from Metadata
    video = pafy.new(url)
    length = video.length

    # Start a chrome session with the Video URL
    pid = subprocess.Popen("google-chrome " + url, shell = True).pid

    # Wait until the video finishes
    time.sleep(length + 5)

    # Terminate the Chrome session
    write_to_file("closed")
    os.killpg(os.getpgid(pid), signal.SIGTERM)