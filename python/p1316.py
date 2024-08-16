count = 0
num = int(input())

for _ in range(num):
    over = []
    s = input()
    
    for j in range(len(s)):
        if s[j] not in over or s[j] == s[j-1]:
            over.append(s[j])
        else:
            break
    
    if len(over) == len(s):
        count = count+1


print(count)
