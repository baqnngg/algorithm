import sys
input = sys.stdin.readline
cnt = 0
puzzle = int(input())
for k in range(2,puzzle):
    if puzzle % k == 0:
        if k > puzzle/k:
            big = k
            small = puzzle/k
        else:
            big = puzzle/k
            small = k
        if big<=3*small:
            cnt+=1
if cnt == 0:
    print("-1")
else:
    print(cnt)