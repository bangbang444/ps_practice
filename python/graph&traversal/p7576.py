import sys

input = sys.stdin.readline

m, n = map(int, input().split())
#행: n # 열:m
box = [list(map(int,input().split())) for _ in range(n)]

from collections import deque

def bfs(box, idxes):
    queue = deque()
    days = 0
    ones = len(idxes)
    for idx in idxes:
        queue.append([idx[0], idx[1], days])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x,y, days = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    ones+=1
                    box[nx][ny] = 1
                    days += 1
                    queue.append([nx,ny, days])
                    days -= 1
                    #print(nx,ny,days)

    return days, ones



idx = []
count = 0
have_zero = False

not_space = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            count += 1
            idx.append([i,j])
        elif box[i][j] == 0:
            have_zero = True
        else:
            not_space+=1

space = n*m - not_space 

days, ones = bfs(box, idx)
print(space, ones)

if have_zero == False:
    print(0)
    exit(0)

if ones != space:
    print(-1)
    exit(0)

print(days)
