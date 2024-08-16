import sys

input = sys.stdin.readline

n = int(input())

chair = [ list(map(int,input().split())) for _ in range(n)]

def special(chair:list):

    space_size = len(chair)
    half = space_size // 2

    if space_size == 1:
        chair.sort()
        return chair[0][0]

    left_top = [row[:half] for row in chair[:half]]
    right_top = [row[half:] for row in chair[:half]]
    left_bottom = [row[half:] for row in chair[half:]]
    right_bottom = [row[:half] for row in chair[half:]]

    
    a = special(left_bottom)
    b = special(left_top)
    c = special(right_bottom)
    d = special(right_top)

    sorted_values = sorted([a, b, c, d])
    return sorted_values[1]

    
print(special(chair))