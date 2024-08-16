# 속도 456ms
import sys

num = int(sys.stdin.readline())

coor = []

for i in range(num):
    coor.append(list(map(int, sys.stdin.readline().split())))

coor.sort()

for i in range(num):
    for j in range(2):
        print(coor[i][j], end =' ')
    print()


'''
주어진 N이 100000이므로 O(NlogN) 안에 해결해야함
이 코드는 4616ms

num = int(input())

coor = []

for i in range(num):
    coor.append(list(map(int, input().split())))

coor.sort()

for i in range(num):
    for j in range(2):
        print(coor[i][j], end =' ')
    print()
'''