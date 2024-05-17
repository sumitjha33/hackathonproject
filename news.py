import requests
import json
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-28&sortBy=publishedAt&apiKey=41307fd3d58849cb9d9f4c88bec43621"
r = requests.get(url)
news = json.loads(r.text)
#print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------")