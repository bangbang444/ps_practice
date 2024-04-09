import sys

input = sys.stdin.readline

left_time, last_time = map(int, input().split())
alcohol = list(map(int, input().split()))

new_alcohol = [0]*(last_time)
new_alcohol.extend(alcohol)

result = 0
accumulated_alcohol = 0

for i in range(left_time):
    accumulated_alcohol += new_alcohol[i+last_time] - new_alcohol[i]
    if 129 <=accumulated_alcohol <= 138:
        result+=1
        continue

print(result)