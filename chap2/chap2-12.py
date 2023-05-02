import requests
from pathlib import Path


# downloadフォルダを作成
out_folder = Path('download')
out_folder.mkdir(exist_ok=True)

# 画像ファイルの取得
image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
img_data = requests.get(image_url)

# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
file_name = image_url.split('/')[-1]
out_path = out_folder.joinpath(file_name)

# 画像データを、ファイルに書き出す
with open(out_path, 'wb') as f:
    f.write(img_data.content)
