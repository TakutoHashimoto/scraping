import requests
from bs4 import BeautifulSoup

url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

