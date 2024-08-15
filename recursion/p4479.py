import sys
input = sys.stdin.readline

def cantor(n):
    
    result = ''
    if n == 0:
        result+='-'
        return result
    
    return cantor(n-1) + " "*(3**(n-1)) + cantor(n-1)

while True:
    try:
        n = int(input())
        print(cantor(n))
    except EOFError:
        break