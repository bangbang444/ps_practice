'''
다익스트라

첫째줄 v,e
둘째줄 시작 노드
셋째줄(u,v,w) 시작->목적지, 가중치
'''

v,e = tuple(map(int, input().split()))
start = int(input())

VE_map = []
weight = 0
result = []
min = 99999999

for i in range(e):
    VE_map.append(tuple(map(int, input().split())))

VE_map.sort()
temp = start


for i in range(1, v+1):

    if i == start:
            result.append(0)
            continue

    for j in range(e):
        
        if VE_map[j][0] == temp:
            temp = VE_map[j][1]
            weight = weight + VE_map[j][2]
            
            if VE_map[j][1] == i:
                if min > weight:
                    min = weight
                break

        

    if weight == 0:
        result.append("INF")
    
    result.append(min)
    weight = 0

    temp = start
        

        
print(result)
