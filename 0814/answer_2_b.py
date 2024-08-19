import requests
from pprint import pprint

# https => http
URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"

response = requests.get(URL)

data = response.json()

data = data['response']['body']['items']
data.append({
    'stationName' : '창준구',
    'pm25Value' : '-'
})
# data를 초 미세먼지에 대해 정렬 
# 초 미세먼지 : pm25Value

def order(city):
    return int(city['pm25Value'])

# 통신장애의 경우, pm25Value가 int값을 가질 수 없어 처리해준다.
# def order(city):
#     pm25Value = city['pm25Value']

#     if pm25Value == '-':
#         # 통신장애.
#         city['pm25Value'] = -1
#     return int(city['pm25Value'])

sorted_data = sorted(data, key=order)

for city in sorted_data:
    print(city['stationName'],city['pm25Value'] )

