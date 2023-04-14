import requests

# WebページをURLで指定して、そのページの情報を取得する
url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)

# 文字化けしないように文字コードを指定する
response.encoding = response.apparent_encoding

# 取得した文字列をテキストファイルに書き込んで保存する
output = "download.txt"
with open(output, 'w') as f:
    f.write(response.text)
