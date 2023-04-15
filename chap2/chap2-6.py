import requests
from bs4 import BeautifulSoup

# 取得したWebページを解析する
url = 'https://www.ymori.com/books/python2nen/test2.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# idで検索して、その中のすべてのliタグを検索して表示する
for element in soup.find(id='chap2').find_all('li'):
    print(element.text)

