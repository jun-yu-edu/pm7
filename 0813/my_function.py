['q', 'w', 'e', 'r']

def my_len(lst):
    # 리스트의 길이
    # 리스트의 원소의 개수

    # 나에게는 개수를 나타내는 변수가 존재해.
    # 그녀석은 0이라는 값을 가지고 있어.

    # 나는 리스트의 원소들을 순회하면서
    # 원소를 만날때마다 개수 변수의 값을 1 늘려줄꺼야.

    count = 0
    for _ in lst:
        count += 1
    return count
    # return lst의 길이를 반환하는 함수를 만들어보세요

def my_sum(lst): # 리스트의 원소는 숫자이다를 가정합니다.
    total = 0
    for num in lst:
        total += num
    return total
    # return lst에 들어있는 원소들의 합

def my_max(lst):
    # lst의 첫번째 원소와 max_value의 초기값을 비교하면
    # 반드시 첫번째 원소가 커야해.

    # 음의 무한대
    # max_value = float('-inf')

    max_value = lst[0] # 원래는 lst의 원소가 존재한다 라는 가정이 필요하긴 합니다.

    for num in lst:
        # num, max_value 을 비교해서 더 큰 값을 max_value 재할당 할꺼야.
        if num > max_value:
            max_value = num

    return max_value

lst = [1, 10, 7, 3, 13]
lst = [-100, -32, -1]
print(my_max(lst))