import requests
while True:
    print(requests.get('https://www.naver.com').text)
    time.sleep(1)

# 1. beautifulsoup4 - static html 파일 => parsing해주는 라이브러리
# 2. selenium - 브라우져를 직접 열어서 동적인 화면을 parsing해주는 라이브러리.


keyword = ['08/14', '8월 14일' '8월14일']

for 게시글 in 게시판:
    제목 = 게시글의 제목
    # 제목에 내가 원하는 키워드가 들어있는 것들을 필터링하고싶어.
    if keyword in 제목:
        원하는게 들어있어.