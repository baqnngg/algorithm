# 5번 =========== bisect , 최장 증가 부분 수열  | 처음배움 ㄷㄷ
import bisect
N = int(input()) 
difficulty = list(map(int, input().split()))
lis = []
for diff in difficulty:
    pos = bisect.bisect_left(lis, diff)
    if pos == len(lis):
        lis.append(diff)
    else:
        lis[pos] = diff
print(len(lis))