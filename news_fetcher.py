import requests
from config import API_KEY

def fetch_top_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "country": "us"  # You can change the country code as per your preference
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["articles"]

top_news = fetch_top_news()
for news in top_news:
    print(news["title"])
    print(news["description"])
    print("=" * 50) 