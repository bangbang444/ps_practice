import sys

input = sys.stdin.readline

a, d, k = map(int, input().split()) # 한판 시간 a, 처음이길확률d, 승률이 전보다 k%오른다.

d, k = d/100, k/100

expected_value = 0
lap = 1
step_probability = 1

while True:
    expected_value += (a*lap) * (step_probability * d)
    step_probability = step_probability * (1-d)
    d *= (1+k)
    lap+=1

    if d >= 1:
        expected_value += (a*lap) * step_probability
        break

print(f'{expected_value:.7f}')