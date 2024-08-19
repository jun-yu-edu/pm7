# 1. api endpoint를 활용해서 URL을 만든다.
BASE_URL = "https://api.themoviedb.org/3/movie"
URL = "/popular"


params = {
    "api_key" : "eab8c9893e725b2e167187cef66bae3d",
    "language" : "ko"
}
# 2. 브라우져에 복붙해서 엔터를 친다
    # 요청
import requests

response = requests.get(BASE_URL + URL, params=params)

# 3. 화면에 정보가 뜬다
    # 응답

from pprint import pprint
data = response.json()