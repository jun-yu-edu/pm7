import requests
from pprint import pprint

# https => http
URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"

response = requests.get(URL)

data = response.json()

data = data['response']['body']['items']


# for city in data:
#     if city['stationName'] == '중구':
#         print('중구찾음')
# for city in data:
#     if city['stationName'] == '관악구':
#         print('관악구찾음')

# dict로 만들면 중구, 관악구에 바로 접근이 가능하다.

dic_data = {}
for city in data:
    # city들을 딕셔너리에 새로 집어넣겠다.
    stationName = city['stationName']

    dic_data[stationName] = city

pprint(dic_data['관악구'])
pprint(dic_data['중구'])

# index를 넣을 경우, data[dic_data['관악구']]




dic_data = {}
for city in data:
    # city들을 딕셔너리에 새로 집어넣겠다.
    stationName = city['stationName']

    city_data = {}

    for key, value in city.items():
        if value is not None:
            city_data[key] = value
    # city_data = {key : value for key, value in city.items() if value is not None}  

    dic_data[stationName] = city_data

pprint(dic_data['관악구'])
pprint(dic_data['중구'])