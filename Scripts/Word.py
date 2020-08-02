import requests

target_word = 6969
current_word = 2

cookies = {
    "bitlagoon": "yourcookiehere"
}
url = "https://www.mrriddle.com/phone/api/get-word"

data = {
	"action": "next"
}

while current_word <= target_word:
	start = requests.post(url, cookies=cookies, data=data)
	#print(start.json()["data"]["word"])		#Uncomment to see each word, this can cause random errors
	#print(current_word)						#Uncomment to see the number your on
	current_word = current_word + 1


print(start.json()["data"]["word"])