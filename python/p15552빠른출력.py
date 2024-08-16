"""
p15552 : 빠른 입출력
sys.stdin.readline()

sys.stdin.readline()는 한 줄 단위로 입력받음
=> 개행문자도 입력됨
rstrip() - 문자열에 오른쪽 공백이나 인자가 된 문자열의 모든 조합 제거
lstrip() - 문자열에 왼쪽 공백이나 인자가 된 문자열의 모든 조합 제거
strip() - 문자열에 양쪽 공백이나 인자가 된 문자열의 모든 조합 제거

이 문제는 strip()이 필요없는 것 같다.
"""
import sys


s = int(sys.stdin.readline().rstrip())
for i in range(s):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(a+b)

