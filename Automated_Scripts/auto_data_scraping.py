import os
import csv
import requests
from bs4 import BeautifulSoup

#Defining the ath where t store the data after scraping
path = '/Users/lohitakshverma/web-scraping-scripts/Automated_Scripts/scraped_data.csv'

# Check wether the same file is not present
os.makedirs(os.path.dirname(path), exist_ok = True)

#Sending the request to the server to scrape data
url = 'https://www.cnn.com'
resp = requests.get(url)

#Parsing the HTML content of the webpage
soup = BeautifulSoup(resp.text, 'html.parser')

#Open the CSV file to write the data
with open(path, 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Tilte','Link'])

    articles = soup.find_all('a', href=True)

    for article in articles:
        title = article.get_text(strip=True)
        link = article['href']

        if link.startswith('/'):
            link = 'https://www.cnn.com/' + link
        
        if title and link:
            writer.writerow([title, link])

print(f"Data Saved at {path}")