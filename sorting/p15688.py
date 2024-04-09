import sys

input = sys.stdin.readline

n = int(input())

arr = [0]*2000001
idx = set()

for i in range(n):
    a = int(input())
    arr[a] += 1
    idx.add(a)

idx = sorted(list(idx))

for i in idx:
    for j in range(arr[i]):
        print(i)
