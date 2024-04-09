"""
# 백준 2798 [브론즈 2] - 파이
# 카드 n장이 주어질 때 3장의 합이 m에 최대한 가까워야 함 
# 3장의 합은 m을 넘으면 안됨
# 맞으면 종료

"""

import itertools

n, m = map(int,input().split())
cardList = []


cardList = list(map(int,input().split()))

card3List = map(list, itertools.combinations(cardList, 3))
diff = sum3 = 300000

for card3 in card3List:
    new_diff = m -sum(card3)
    
    if new_diff == 0:
            sum3 = sum(card3)
            break

    if new_diff > 0:
        if diff > new_diff:
            diff = new_diff
            sum3 = sum(card3)

print(sum3)