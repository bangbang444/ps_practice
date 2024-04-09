import sys

input = sys.stdin.readline
# A: 상승, B: 미끄러짐, V: 높이

a,b,v = map(int,input().split())
state = 0
day = 0

goal = v - a # goal보다 커지는데 며칠이 걸리냐


least = goal//(a-b)
pre_last = least * (a-b)

if pre_last+a >= v:
    print(least+1)
else:
    i = 1
    while True:
        if pre_last+a >= v:
            print(least+i)
            break
        pre_last += a-b
        i+=1
