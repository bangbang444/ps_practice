'''
import sys

input = sys.stdin.readline

n, q = int(input())
cost = list(map(int, input().split()))
'''


def pow(a, b, m):
	if(b==1): 
		return a & m
	val = pow(a, b//2, m)
	if(b%2 == 0): 
		return val
	return val * a % m

a,b,c = map(int,input().split())
print(pow(a,b,c))