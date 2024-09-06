# from itertools import combinations
# n,h = map(int,input().split())
# arr = [int(input()) for _ in range(n)]
# j = 1
# c = 1
# pp = []
# arr.sort()
# while 1:
#     for i in combinations(arr, j):
#         if sum(i) >= h:
#             c += 1
#             pp.append(sum(i))
#     if c > 1:
#         break
#     j+=1
# print(min(pp)-h)

# 선생님 DFS
# import sys
# sys.setrecursionlimit
# input = sys.stdin.readline

# n,h = map(int,input().split())
# l = [int(input()) for _ in range(n)]
# ans = 999999

# def back(x, sum):
#     global ans
#     if sum>=h:
#         if ans>sum-h:
#             ans=sum-h
#         return

#     if x == n:
#         return
    
#     back(x+1, sum)
#     back(x+1, sum+l[x])

# back(0,0)
# print(ans)

# 선생님 BFS
