# 1번
# n = int(input())
# S = list(map(float,input().split()))
# print("%.1f\n%.1f" %(sum(S),(sum(S)/len(S))))


# 2번 ------- 피보나치 수열
# n = int(input())
# dp = [0] * (n+1)
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])


# 3번 ---------------- 진수변환 중요
# n = int(input())
# def solution(n, q):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
#     return rev_base[::-1] 
# print(solution(n, 2))
# print(solution(n, 3))
# print(solution(n, 4))


# 4번 -------------- ord, chr 중요
# a = input()
# b = input()
# for i in b:
#     c = ord(i)-ord('a')
#     if c < 0:
#         print(" ",end="")
#     else:
#         print(a[c],end="")


# 5번 =========== bisect , 최장 증가 부분 수열  | 처음배움 ㄷㄷ
# import bisect
# N = int(input()) 
# difficulty = list(map(int, input().split()))
# lis = []
# for diff in difficulty:
#     pos = bisect.bisect_left(lis, diff)
    
#     if pos == len(lis):
#         lis.append(diff)
#     else:
#         lis[pos] = diff
# print(len(lis))


# 6번 ----------- 트리구조
# def haha(sn):
#     visited[sn] += 1
#     for i in adj_list[sn]:
#         if visited[i] != 1:
#             haha(i)
# n = int(input())
# p = int(input())
# adj_list = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# for _ in range(p):
#     s,e = map(int,input().split())
#     adj_list[s].append(e)
#     adj_list[e].append(s)
# t = int(input())
# haha(t)
# print(visited.count(1)-1)


# 7번 ========= 다익스트라 숙지

# 8번 ============= 힙트리?가 뭐임?