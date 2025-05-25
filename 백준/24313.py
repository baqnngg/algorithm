#알고리즘 수업 - 점근적 표기 1
a1,a2 = map(int,input().split())
c = int(input())
n = int(input())
if (a1*n + a2) <= (c*n) and a1 <= c: print(1)
else: print(0)