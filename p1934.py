# 유클리드 호제법으로 최대공약수 
# 최소공배수: 두 수의 곱 / 최대공약수
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    mul = a*b
    big = max(a,b)
    small = min(a,b)

    while small != 0:
        rest = big % small
        big = small
        small = rest
    
    print(mul // big)
