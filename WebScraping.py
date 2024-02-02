import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'YOUR_TARGET_URL'

# Send a HTTP request to the specified URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find elements by their tag and class (modify as per your target elements)
    titles = soup.find_all('h2', class_='your-target-class')
    
    # Iterate through the found elements and print their text content
    for title in titles:
        print(title.get_text().strip())
else:
    print('Failed to retrieve the webpage')

