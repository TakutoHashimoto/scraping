import requests
from bs4 import BeautifulSoup

# 取得したWebページを解析する
url = 'https://www.ymori.com/books/python2nen/test2.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# ページのすべてのliタグを検索して、その文字列を表示する
for element in soup.find_all('li'):
    print(element.text)
