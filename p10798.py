import sys

input = sys.stdin.readline

row = 5

str_list = []
result = [-1] * 75


for i in range(5):
    str_list.append(input())


for i in range(row):
    leng =len(str_list[i])
    for j in range(leng):
        result[i+j*leng] = str_list[i][j]

print(result)
a=''
for i in result:
    if i != -1 and i != '\n':
        a+=i
print(a)
