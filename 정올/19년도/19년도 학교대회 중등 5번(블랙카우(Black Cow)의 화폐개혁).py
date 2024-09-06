a = int(input())
b = []
for i in range(1,a):
    if a%i == 0:
        b.append(i)
print(a,max(b),min(b))