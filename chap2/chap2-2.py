import requests
from bs4 import BeautifulSoup

url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# title, h2, liタグを検索して表示する
print(soup.find('title'))
print(soup.find('h2'))
print(soup.find('li'))
