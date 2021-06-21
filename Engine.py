# Utility Program to call Actual Assistant
import speech_recognition
import gtts
import os
import time

# Write your own Wake word
wake_word = "jarvis"

def main():
    os.chdir("Assistant")
    recogniser = speech_recognition.Recognizer()
    while True:
        time.sleep(0.2)
        flag = True
        try:
            with speech_recognition.Microphone() as mic:
                recogniser.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recogniser.listen(mic)
                text = recogniser.recognize_google(audio)
                text = text.lower()
                flag = wake_word in text
                if flag:
                    os.system("python3 Assistant.py")
        except:
            continue

if __name__ == '__main__':
    main()