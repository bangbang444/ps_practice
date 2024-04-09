# 하노이
import sys

input = sys.stdin.readline

n = int(input())

move_path = []
def hanoi(start,end,disk): # 원판 n개를 a에서 b로
    move_count=0
    middle = 6 - start - end

    if disk == 1:
        move_count+=1
        print(start, end)
        return
    
    hanoi(start, middle, disk-1)
    print(start, end)
    hanoi(middle, end, disk-1)

    return move_count


print(2**n-1)    
hanoi(1,3,n)


'''
맨 밑을 3번째로 옮기고
자기 위를 옆으로 옮긴다.

처음 중간 끝

중간 또는 처음이 비어있다면 끝으로 옮긴다.
'''
    

