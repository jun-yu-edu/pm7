import requests

response = requests.get('http://127.0.0.1:8000/articles/')

from pprint import pprint

# pprint(response.json())

for data in response.json():
    print(data.get('title'))