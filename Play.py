#!/usr/bin/python3
# Plays Music in VLC
# Dependencies: Aliasing
import os
import sys

vlc_files = [".flac",".mp3",".wav",".mp4",".og"]
os.chdir("/home/suman/")
dir_path = os.path.dirname(os.path.realpath("."))
keys = sys.argv[1:]
results = []
for root,dirs,files in os.walk(dir_path):
    for file in files:
        if all([item.lower() in str(file).lower() for item in keys]) and any([format in file for format in vlc_files]):
            temp = (root+'/'+str(file))
            results.append(os.path.realpath(temp))
for i in range(len(results)):
    print(i+1,results[i])
if len(results)==1:
    index = 1
else:
    index = int(input("Enter Index: "))
file = results[index-1]
if any([i in file for i in vlc_files]):
    file = '"'+file+'"'
    os.system("vlc "+file)
