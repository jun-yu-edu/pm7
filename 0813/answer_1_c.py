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

# 모든 영화를 확인하여 평점이 7 이상인 영화를 고르것이다.
over_7_movies = []
for movie in data:
    vote_average = movie['vote_average']

    # 만약 vote_count가 특정 값보다 작으면 실행하지 마.
    vote_count = movie['vote_count']

    if vote_average >= 7:
        # 그 영화는 7 이상이야.
        # print(movie['title'])
        title = movie['title']
        over_7_movies.append(title)


print(over_7_movies)



####################################################################
# 투표수 100 미만 거르기

# 모든 영화를 확인하여 평점이 7 이상인 영화를 고르것이다.
over_7_movies = []
for movie in data:
    vote_average = movie['vote_average']

    # 만약 vote_count가 특정 값보다 작으면 실행하지 마.
    vote_count = movie['vote_count']

    if vote_count < 100:
        print(movie['title'])
        print(vote_count, vote_average)
        continue # 아래 코드 실행하지 마 / 다음 반복 실행해.

    if vote_average >= 7:
        # 그 영화는 7 이상이야.
        # print(movie['title'])
        title = movie['title']
        over_7_movies.append(title)

    # if vote_count >= 100:
    #     if vote_average >= 7:
    #         # 그 영화는 7 이상이야.
    #         # print(movie['title'])
    #         title = movie['title']
    #         over_7_movies.append(title)


print(over_7_movies)


###################################################
# list comprehension
over_7_movies = [movie['title'] for movie in data if movie['vote_average'] >= 7]


# # 아래의 4줄의 코드가 그 아래 1줄 코드와 완벽히 일치.
# 이때, el는 value를 활용한 새로운 변수(또는 활용하지 않아도 괜찮습니다.)
# new_lst = []
# for value in lst:
#     if condition:
#         new_lst.append(el)

# # new_lst = [el for value in list if condition]

# # condition 생략 버전
# new_lst = []
# for value in lst:
#     new_lst.append(el)

# # new_lst = [el for value in list]