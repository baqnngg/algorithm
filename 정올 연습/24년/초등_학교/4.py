# 카드놀이
n = int(input())
a = [i for i in range(1, n+1)]
b = 0
while a:
    b = a.pop(0)
    a.append(b)
    a.pop(0)
print(b)