import requests
from bs4 import BeautifulSoup
import urllib


load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 全てのimgタグを検索して、リンクを取得する
for element in soup.find_all("img"):
    src = element.get("src")

    # 絶対URLとファイルを表示する
    image_url = urllib.parse.urljoin(load_url, src)
    file_name = image_url.split("/")[-1]

    print(f"{image_url} >> {file_name}")
