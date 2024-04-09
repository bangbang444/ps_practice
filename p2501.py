import sys

input = sys.stdin.readline

a, b = map(int, input().split())
divisor = []

end = a//2+1
for i in range(1, end):
    if a % i == 0:
        divisor.append(i)

divisor.append(a)
if len(divisor) >= b:
    print(divisor[b-1])
else:
    print(0)
