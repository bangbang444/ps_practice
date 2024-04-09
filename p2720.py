import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    rest = int(input())

    quarter = rest//25
    rest = rest%25

    dime = rest//10
    rest = rest%10

    nickel = rest//5
    rest = rest%5

    penny = rest
    print(quarter, dime, nickel, penny)