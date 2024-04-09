import sys

input = sys.stdin.readline

T = int(input())


def rest(a, b):

    if b == 1:
        return a%10
    
    val = rest(a, b//2)
    if b % 2 == 0:
        return val * val % 10
    else:
        return val*val*a%10

for i in range(T):
    a, b = map(int, input().split())

    result = rest(a,b)

    if result == 0:
        print(10)
    else:
        print(result)