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

# def order(city):
#     pm25Value = city['pm25Value']

#     if pm25Value == '-':
#         # 통신장애.
#         city['pm25Value'] = -1
#     return int(city['pm25Value'])

sorted_data = sorted(data, key=order)

for city in sorted_data:
    print(city['stationName'],city['pm25Value'] )


################################################################################################

# ####### 통신장애가 일어났을 때
# # 1. some flag : "통신장애"
# # 2. pm25Value : "-"

# # 하고싶은 것 : pm25 value 순으로 정렬.

# # for datum in data:
# #     if 통신장애:
# #         # 그 데이터를 삭제해.
# #         # 주변 데이터를 바탕으로 예상해.
# #         # 이전 데이터를 바탕으로 예상해.


# 이상있는 데이터를 임의의 값으로 바꿈(실제 상황에서는 좋지 못할 수 있습니다.)

# def order(city):
#     pm25Value = city['pm25Value']

#     if pm25Value == '-':
#         # 통신장애.
#         city['pm25Value'] = 0
#     return int(city['pm25Value'])

# sorted_data = sorted(data, key=order)

# for city in sorted_data:
#     print(city['stationName'],city['pm25Value'] )



# 데이터를 삭제하고 싶을 때는
# 새로운 데이터를 마련한다.

clean_data = []

for datum in data:
    if datum 통신장애가 아니라면:
        clean_data.append(datum)
# filter
# 함수로 묶어다가 만드는 것이 좋습니다.
# 이제부터 clean_data를 사용하겟어.

####################################################################################

# 실제 처리할 때는 sort에 임의로 넣는 것이 아니라, data 자체를 처리하는 것이 좋습니다.

# def clean(data):
#     data = 통신장애 처리 함수(data)
#     data = 기기장애 처리 함수(data)
#     data = 이상값 처리(data)
#     data = ...
#     return clean_data


small_data = []
for city in data:
    pm25Value = city['pm25Value']
    staionName = city['staionName']

    small_data.append( [pm25Value, staionName] )
