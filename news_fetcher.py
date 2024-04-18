import requests

def fetch_top_news(api_key):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "us"  # You can change the country code as per your preference
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["articles"]

# Replace 'your_api_key' with your actual News API key
api_key = '238f84865d5f4a4d83ae456c009d2961'
top_news = fetch_top_news(api_key)
for news in top_news:
    print(news["title"])
    print(news["description"])
    print("=" * 50) 