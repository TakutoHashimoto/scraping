import requests
from bs4 import BeautifulSoup
import urllib

load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

output = 'link_list.txt'
with open(output, 'w') as f:
    # すべてのaタグを検索して、リンクを絶対URLでファイルに書き込む
    for element in soup.find_all('a'):
        url = element.get('href')
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(f'{element.text}: {link_url}\n')

