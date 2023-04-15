import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
url = 'https://news.yahoo.co.jp/categories/it'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# classで検索して、その中のすべてのaタグを検索して表示する
for element in soup.find(class_='sc-fQvxkG hovjdV').find_all('a'):
    print(element.text)

