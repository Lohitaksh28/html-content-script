from bs4 import BeautifulSoup
import requests

url = 'https://bbc.com' 

response= requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print("Page Title:", soup.title.string.strip())

for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    print(heading.get_text())

for link in soup.find_all('a'):
    print(link.get('href'))