import sys


input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = [0] * (N+M)
a = 0
b = 0

for i in range(N+M):
    if A[a] <= B[b]:
        print(A[a], end=' ')
        a+=1
    else:
        print(B[b], end=' ')
        b+=1
    
    if a == N:
        while b != M:
            print(B[b], end=' ')
            b+=1
        break
    elif b == M:
        while a != N:
            print(A[a], end=' ')
            a+=1
        break



