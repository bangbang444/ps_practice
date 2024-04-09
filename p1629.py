import sys

input = sys.stdin.readline


def pow_rest(a,b,c):
    if b == 1:
        return a % c
    
    rest = pow_rest(a,b//2,c)
    if b %  2 == 0:
        return (rest * rest) % c
    else:
        return (rest * rest * a) % c

    
# A^B%C
a,b,c = map(int, input().split())
print(pow_rest(a,b,c))


# 제곱 수의 합
# 나머지의 곱 % m = 답
'''
2147483647 2147483647 100001 => 7569
7^6%5 = 4
7^5%5 = 2
7^4%5 = 1
7^3%5 = 3
7^2%5 = 4
7^1%5 = 2


'''


'''
잘못된 예
if b %  2 == 0:
        return pow_rest(a,b//2,c) * pow_rest(a,b//2,c) % c
    else:
        return pow_rest(a,b//2+1,c) * pow_rest(a,b//2,c) % c
'''