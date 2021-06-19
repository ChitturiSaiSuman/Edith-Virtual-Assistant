# importing requests package
import requests
import time
from gtts import gTTS
from playsound import  playsound
def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "07f766d391d946aa9582e87a1f3dd9ae"
	}
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
		
		# printing all trending news
		print(i + 1, results[i])
		myobj=gTTS(text=results[i],lang='en')
		myobj.save("welcome1.mp3")
		playsound("welcome1.mp3")

# Driver Code
if __name__ == '__main__':
	NewsFromBBC()
