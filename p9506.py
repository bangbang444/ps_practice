import sys

input = sys.stdin.readline

n = int(input())
while n != -1:
    divisor = []
    end = n // 2
    while True:
        for i in range(1, end+1):
            if n % i == 0:
                divisor.append(i)
        break

    if sum(divisor) == n:
        print(f"{n} = ", end= "")
        for i in range(len(divisor)-1):
            print(divisor[i], "+ ", end="")
        print(divisor[-1])
            
    else:
        print(f"{n} is NOT perfect.")


    n = int(input())