import sys

input = sys.stdin.readline

n = int(input())

coor = []
for i in range(n):
    coor.append(list(map(int,input().split())))


coor = sorted(coor, key = lambda y : (y[1], y[0]))

for x,y in coor:
    print(x, y)