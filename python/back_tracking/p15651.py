import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * m
is_used = [0] * (n+1)

def sequence(k):

    if k == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr[k] = i
        sequence(k+1)

sequence(0)