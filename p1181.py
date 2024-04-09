import sys

input = sys.stdin.readline

n = int(input())

word_list = []
for i in range(n):
    word_list.append(input()[:-1])

word_list = list(set(word_list))

results = sorted(word_list, key = lambda x : (len(x), x))

for result in results:
    print(result)