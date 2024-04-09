import sys

input = sys.stdin.readline

n = int(input())

def factorial(n : int):
    val = 1
    
    if n == 0 or n == 1:
        return 1
    
    val*=n
    return val * factorial(n-1)


print(factorial(n))