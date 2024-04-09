import sys

input = sys.stdin.readline

n, k = map(int, input().split())

h = 0
m = 0
s = 0

count = 0
while n >= h:
    h1 = h // 10
    m1 = m // 10
    s1 = s // 10
    h2 = h % 10
    m2 = m % 10
    s2 = s % 10

    if k == h1 or k == m1 or k == s1 or k == h2 or k == m2 or k == s2:
        count += 1

    s+=1
    if s == 60:
        s = 0
        m += 1

        if m == 60:
            m = 0
            h += 1

print(count)