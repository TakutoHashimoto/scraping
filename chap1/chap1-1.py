import requests

# WebページをURLで指定して、そのページの情報を取得する
url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)

# 文字化けしないように文字コードを指定する
response.encoding = response.apparent_encoding

# 取得した文字列を表示する（HTMLデータが表示される）
print(response.text)
