import json
from pprint import pprint


with open("chap5/test2.json", mode="r") as f:
    json_data = json.loads(f.read())
    pprint(json_data)
