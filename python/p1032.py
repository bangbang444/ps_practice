import sys

input = sys.stdin.readline

n = int(input())

name = list(input())
result = name
for i in range(n-1):
    name2 = list(input())

    for i in range(len(name)):
        if name[i] == name2[i]:
            continue
        else:
            result[i] = '?'

result = result[:-1]
print(''.join(result))

