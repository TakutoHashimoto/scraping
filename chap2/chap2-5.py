import requests
from bs4 import BeautifulSoup

# 取得したWebページを解析する
url = 'https://www.ymori.com/books/python2nen/test2.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# idで検索して、そのタグの中身を表示する
chap2 = soup.find(id='chap2')
print(chap2)
