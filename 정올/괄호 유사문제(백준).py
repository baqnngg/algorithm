# 야메
# a = int(input())
# for _ in range(a):
#     b = list(input())
#     if len(b) % 2 == 0:
#         for i in range(len(b)):
#             if b[i] == "(":
#                 for j in range(i+1,len(b)):
#                     if b[j] == ")":
#                         b[i] = 0 
#                         b[j] = 0
#                         break
#         if b.count("(") == 0 and b.count(")") == 0:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

# 프로그레머스
# def solution(a):
#     s = list(a)
#     answer = False
#     if len(s) % 2 == 0:
#         for i in range(len(s)):
#             if s[i] == "(":
#                 for j in range(i+1,len(s)):
#                     if s[j] == ")":
#                         s[i] = "0" 
#                         s[j] = "0"
#                         break
#         if s.count("(") == 0 and s.count(")") == 0:
#             answer = True
#         else:
#             answer = False
#     else:
#         answer = False
#     return answer

# 스택으로 하는법
def solution(s):
    stack = [] # 파이썬에서 stack은 1차원 리스트로 구현(또는 재귀함수->DFS)
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True