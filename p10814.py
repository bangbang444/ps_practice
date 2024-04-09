import sys

input = sys.stdin.readline

n = int(input())
info_list = []
i = 0
for i in range(n):
    age, name = input().split()
    age = int(age)

    info_list.append([age, name, i])
    i+=1

results = sorted(info_list, key = lambda x : (x[0], x[2]))

for result in results:
    print(result[0], result[1])