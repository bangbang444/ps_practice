# DP, 1로 만들기
# 3,2 나누기, -1해서 1만들기
import sys

input = sys.stdin.readline

D = [0] * 1000001

D[1] = 0

n = int(input())

for i in range(2, n+1):
    D[i] = D[i-1] + 1
    if(i%2 == 0): D[i] = min(D[i], D[i//2] + 1)
    if(i%3 == 0): D[i] = min(D[i], D[i//3] + 1)



print(D[n])