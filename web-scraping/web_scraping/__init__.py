import requests
from bs4 import BeautifulSoup
import re

def scrape_sentences_with_keyword(url, keyword):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all paragraphs in the main content area
        paragraphs = soup.find_all('p')

        # Loop through each paragraph to extract sentences containing the keyword
        for paragraph in paragraphs:
            # Split the paragraph into sentences using regex
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph.text)
            for sentence in sentences:
                # Check if the keyword is present in the sentence
                if keyword.lower() in sentence.lower():
                    print(sentence.strip())
    else:
        print("Failed to retrieve webpage:", response.status_code)

# URL of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Keyword to search for in sentences
keyword = "scraping"

# Call the function to scrape sentences with the keyword
scrape_sentences_with_keyword(url, keyword)