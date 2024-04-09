# 138페이지 
import sys

input = sys.stdin.readline

h, w = map(int, input().split())

block = list(map(int,input().split()))
total_rainwater = 0
rainwater = 0
a_list = []
# start semi semi ... end

start = -1
start_idx = -1
ground_count = 0
ground = -1
middle_start = start
middle_idx = 0

for i in range(w):
    if block[i] >= start: # 균형있는 U - start <= end
        for j in range(start_idx+1, i):
            total_rainwater += start - block[j]
        start = block[i] # 제일 높은 곳
        start_idx = i
        middle_start = start
        middle_idx = start_idx
        ground_count = 0
        ground = -1
        rainwater = 0
        continue

    # start > end
    


    # if block[i] > ground:
    #     ground = block[i]
    #     ground_count += 1
    
    # if ground_count == 2:
    #     for j in range(middle_idx+1, i):
    #         rainwater += block[i] - block[j]
    #         print("hi", block[i], block[j], i)
    #     middle_idx = i
    #     middle_start = block[i]
    #     ground_count = 0
    #     ground = -1
        
        

        
total_rainwater += rainwater
print(total_rainwater)





    


        

