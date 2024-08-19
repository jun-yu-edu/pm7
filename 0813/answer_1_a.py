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
pprint(data)
# [ 영화1, 영화2, 영화3, 영화4, {}]

max_vote_average = 0
for movie in data:
    vote_averge = movie['vote_average']

    if vote_averge > max_vote_average:
        max_vote_average = vote_averge

        max_vote_average_movie = movie

print(max_vote_average)
pprint(max_vote_average_movie)