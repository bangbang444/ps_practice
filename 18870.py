'''
아직 못풂
'''
import sys

num = int(sys.stdin.readline())

input_list = list(map(int,sys.stdin.readline().split()))

result = [0] * num

for i in range(num):
    for j in range(num):
        if input_list[i] > input_list[-j]:
            result[i] += 1 


for i in result:
    print(i, end=' ')

# 2 4 -10 4 -9 / 2 3 0 3 1