# 1번 -- 규칙성(하노이탑)
# n = int(input())
# print((2**n)-1)


# 2번 -- 어떤 규칙을 갖는지 잘 보자(이거는 1이 몇개인지)
# n = list(map(int,input().split()))
# t = []
# for i in range(len(n)-1):
#     if n[i] == 0:
#         continue
#     for j in range(i+1,len(n)):
#         if n[i] != n[j]:
#             t.append(j-i)
#             t.append(n[i])
#             break
#         else:
#             n[j] = 0
# print(*t)
