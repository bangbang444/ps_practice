# 다시 풀기
import itertools

height_list = [int(input()) for _ in range(9)]

height_7 = map(list,itertools.combinations(height_list, 7))


for dwarf7 in height_7:
    
    if len(set(dwarf7)) != 7:
        continue

    if sum(dwarf7) == 100:
        for dwarf in dwarf7:
            if dwarf <=0 or dwarf >= 100:
                break
        
        dwarf7.sort()
        for dwarf in dwarf7:
            print(dwarf)
            