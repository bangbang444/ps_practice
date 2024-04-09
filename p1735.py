import sys

input = sys.stdin.readline

def gcd(big, small):
    while small != 0:
        rest = big % small
        big = small
        small = rest
    return big

numberator1, denominator1 = map(int, input().split())
numberator2, denominator2 = map(int, input().split())

# 더하기
big = max(denominator1, denominator2)
small = min(denominator1, denominator2)
mul = big*small
gcd1 = gcd(big, small)

denominator = mul//gcd1 # 곱 / 최소공배수
nominator = numberator1*denominator//denominator1 + numberator2*denominator//denominator2

# 기약분수
gcd2 = gcd(nominator, denominator)
print(nominator//gcd2, denominator//gcd2)

