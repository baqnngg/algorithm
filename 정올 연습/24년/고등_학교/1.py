# 대진표 만들기
from itertools import permutations
import sys
input = sys.stdin.readline

n,d = map(int,input().split())
arr = list(map(int,input().split()))
possible = []
for i in permutations(arr, 2):
    if abs(i[0]-i[1]) <= d or abs(i[1]-i[0]) <= d:
        possible.append(i)

print(len(possible))