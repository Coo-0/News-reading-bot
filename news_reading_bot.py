import requests

# Set up the news API endpoint and API key
url = 'https://newsapi.org/v2/top-headlines'
api_key = 'YOUR_API_KEY_HERE'

# Define the news source and parameters for the API call
params = {
    'sources': 'bbc-news',
    'pageSize': 5
}

# Make the API request and parse the JSON response
response = requests.get(url, params=params, headers={'Authorization': 'Bearer ' + api_key})
articles = response.json()['articles']

# Print out the article titles and descriptions
for article in articles:
    print(article['title'])
    print(article['description'])
    print()
