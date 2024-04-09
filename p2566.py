m = 0

for i in range(9):
    lst = list(map(int,list(input().split())))

    max_new = max(lst)

    if m <= max_new:
        m = max_new
        x = i+1
        y = lst.index(max_new) + 1
        

print(m)
print(x, y)
