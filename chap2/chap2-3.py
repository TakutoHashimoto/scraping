import requests
from bs4 import BeautifulSoup

# 取得したWebページを解析する
url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# title, h2, liタグを検索して文字列だけ表示する（タグは表示しない）
print(soup.find('title').text)
print(soup.find('h2').text)
print(soup.find('li').text)
