import requests

# 画像ファイルを取得する
image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
img_data = requests.get(image_url)

# URLからファイル名を取り出す
file_name = image_url.split('/')[-1]

with open(file_name, 'wb') as f:
    f.write(img_data.content)
