# 경품
n = int(input())
a = list(map(int, input().split()))
b = len(a)
a = set(a)
print(b-len(a))