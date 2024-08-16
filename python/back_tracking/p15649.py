# N과 M(1)
import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # N 최대치, M 개수

arr = [0]*10
is_used = [0]*10
leng = len(arr)-1

def sequence(k):

    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        if is_used[i] == 0:
            arr[k] = i
            is_used[i] = 1
            sequence(k+1)
            is_used[i] = 0    

sequence(0)