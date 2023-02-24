import requests
import pyttsx3

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

# Set up text-to-speech engine
engine = pyttsx3.init()

# Loop through each article and read it out loud
for article in articles:
    # Extract the article title and description
    title = article['title']
    description = article['description']
    
    # Read the article title and description out loud
    engine.say(title)
    engine.say(description)
    engine.runAndWait()
