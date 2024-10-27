a = int(input())
b = []
for i in range(2, a):
    if a % i == 0:
        b.append(i)

if len(b) == 2:
    if 4 in b:
        print("wrong number")
    else:
        print(*b)
else:
    print("wrong number")