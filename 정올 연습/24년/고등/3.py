# 비밀번호

from itertools import product

n = int(input())
a = list(map(int, input().split()))
b = []

for i in product(a ,repeat=4): b.append(i)
b.sort()

for i in b:  print(f"{i[0]}{i[1]}{i[2]}{i[3]}")