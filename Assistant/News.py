# Reads out News Headlines from BBC
import requests
import gtts
import playsound
import os

def NewsFromBBC():
	
	# BBC news api
	# Following query parameters are used
	# source, sortBy and apiKey

	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "<Your API Key>"
	}

	# URL of News API
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# Convert Text to Speech using Google Text-to-speech Engine
		myobj = gtts.gTTS(text = results[i], lang = 'en')

		# Save it in Mp3 Format
		myobj.save("News.mp3")

		# Play the music file
		playsound.playsound("News.mp3")

		# Remove the music file after reading
		os.system("rm News.mp3")