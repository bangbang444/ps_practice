
"""
브론즈 1
"""
number = int(input())

minus = 9 * len(list(str(number)))

if(number > 20):
    for i in range(number-minus-1,number):
        decomposition_number = list(map(int, list(str(i))))
        if(i + sum(decomposition_number)) == number:
            print(i)
            exit(0)
else:
    for i in range(1, number+1):
        decomposition_number = list(map(int, list(str(i))))
        if(i + sum(decomposition_number)) == number:
            print(i)
            exit(0)

print(0)