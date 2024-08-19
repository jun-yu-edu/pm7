import requests
from pprint import pprint

BASE_URL = "https://api.themoviedb.org/3/movie"
URL = "/now_playing"


params = {
    "api_key" : "eab8c9893e725b2e167187cef66bae3d",
    "language" : "ko"
}

response = requests.get(BASE_URL + URL, params=params)


data = response.json()

data = data['results']


def order(movie):
    return movie['vote_average']

sorted_data = sorted(data, key=order)
sorted_data = sorted(data, key=lambda movie : movie['vote_average'])

for movie in sorted_data:
    title = movie['title']
    vote_average = movie['vote_average']
    print(f'{title} : {vote_average}')

#######################################################
print()

def order(movie):
    vote_average = movie['vote_average']
    vote_count = movie['vote_count']

    if vote_count >= 100:
        return vote_average
    else:
        return vote_average * 0.8 # 특정 경우 정렬의 weight를 조절할 수 있다.

sorted_data = sorted(data, key=order)

for movie in sorted_data:
    title = movie['title']
    vote_average = movie['vote_average']
    print(f'{title} : {vote_average}')


