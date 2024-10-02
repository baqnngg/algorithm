# 3번 ---------------- 진수변환 중요
n = int(input())
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1] 
print(solution(n, 2))
print(solution(n, 3))
print(solution(n, 4))
