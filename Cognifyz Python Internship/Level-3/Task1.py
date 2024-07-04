import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all book titles and prices (adjust selectors based on the website structure)
        titles = soup.find_all('h2', class_='book-title')
        prices = soup.find_all('span', class_='book-price')
        
        # Print the extracted data
        for title, price in zip(titles, prices):
            print(f"Title: {title.text.strip()} - Price: {price.text.strip()}")

    else:
        print(f"Failed to retrieve page: {response.status_code}")

# Example usage:
url = 'https://example.com/books'  # Replace with the URL of the website you want to scrape
scrape_books(url)
