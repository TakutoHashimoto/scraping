import requests
from bs4 import BeautifulSoup

url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all('a'):
    link_url = element.get('href')
    print(f'{element.text}: {link_url}')
