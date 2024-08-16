import sys

input = sys.stdin.readline

n = int(input())


num_stack = []
stack = []
num = 1
top = -1
for i in range(n):
    p = int(input())

    # if i == 0:
    #     while num != p+1:
    #         num_stack.append(num)
    #         num+=1
    #         stack.append("+")
    #     num_stack.pop()
    #     if len(num_stack) != 0:
    #         top = num_stack[-1]
    #     stack.append("-")
    #     print(stack)
    #     print(num_stack)
    #     continue

    if p == top:
        num_stack.pop()
        stack.append("-")
        #print(stack)
        #print(num_stack)
    elif top < p:
        while num != p+1:
            num_stack.append(num)
            num+=1
            stack.append("+")
        num_stack.pop()
        stack.append("-")
        #print(stack)
        #print(num_stack)
    else:
        if top > p:
             print("NO")
             exit(0)
        while top != p:
            num_stack.pop()
            stack.append("-")
        #print(stack)
        #print(num_stack)
    
    if len(num_stack) != 0:
            top = num_stack[-1]
    elif len(num_stack) == 0 and i != n:
            top = -1
    else:
        break

for i in stack:
    print(i)







    
    
    
