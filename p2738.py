import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

mat1 = []
mat2 = []
result = []

for _ in range(num1):
    mat1.append(list(map(int, input().split())))

for _ in range(num1):
    mat2.append(list(map(int, input().split())))

for idx1 in range(num1):
    for idx2 in range(num2):
        print(mat1[idx1][idx2]+mat2[idx1][idx2], end=' ') 
    print()

