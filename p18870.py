'''
좌표 압축 => 시간초과
'''
import sys

input = sys.stdin.readline

n = int(input())
coor = list(map(int, input().split()))
sorted_coor = sorted(coor)
sorted_coor.insert(0, 0)

for i in range(len(coor)):
    pre_num = sorted_coor[sorted_coor.index(coor[i])-1]
    pre_idx = sorted_coor.index(pre_num)
    
    print(pre_idx, end = " ")

