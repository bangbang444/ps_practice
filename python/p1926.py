import sys

input = sys.stdin.readline

a, b = map(int, input().split())
max_area = 0
area = 0
queue = []
picture = 0
grid = [list(map(int, input().split())) for _ in range(a)]

queue_idx = 0 # 큐 빼기

test = []

for i in range(a):    
    for j in range(b):
        if grid[i][j] == -1 or grid[i][j] == 0:
            continue
        
        x = i
        y = j
        grid[x][y] = -1 # 시작점
        area+=1
        if x-1 >= 0 and grid[x-1][y] != 0:
            queue.append((x-1, y))
        if y-1 >= 0 and grid[x][y-1] != 0:
            queue.append((x, y-1))
        if x+1 < a and grid[x+1][y] != 0:
            queue.append((x+1, y))
        if y+1 < b and grid[x][y+1] != 0:
            queue.append((x, y+1))

        while True:
            if grid[x][y] == -1:
                if queue_idx == len(queue):
                    break
                x, y = queue[queue_idx]
                queue_idx += 1
                continue
            
            grid[x][y] = -1

            if x-1 >= 0 and grid[x-1][y] != 0:
                queue.append((x-1, y))
            if y-1 >= 0 and grid[x][y-1] != 0:
                queue.append((x, y-1))
            if x+1 < a and grid[x+1][y] != 0:
                queue.append((x+1, y))
            if y+1 < b and grid[x][y+1] != 0:
                queue.append((x, y+1))
            
            x, y = queue[queue_idx]
            queue_idx += 1
            area+=1
            
            if queue_idx == len(queue):
                break
        
        if max_area < area:
            max_area = area

        picture += 1
        area = 0

print(picture)
print(max_area)

                

