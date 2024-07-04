import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.bbc.com/news'

# Send a request to fetch the content of the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the headlines - assuming they are in <h3> tags with a class 'gs-c-promo-heading__title'
    headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

    # Print the headlines
    for index, headline in enumerate(headlines):
        print(f"{index + 1}. {headline.get_text()}")
else:
    print("Failed to retrieve the page")

