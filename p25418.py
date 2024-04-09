'''
k에서 a를 맞춰나간다는 생각
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 0
if a == b:
    print(count)
    exit(0)

while True:
    if a == b:
        break

    if a <= b/2:
        if b%2 != 0:
            b-=1
        else:
            b//=2
    else:
        b-=1
    
    count+=1

    
print(count)