from itertools import product

a = int(input())
nums = list(map(int,input().split()))
c = []
for i in product(nums, repeat=4):
    c.append(i)

c.sort(reverse=False)

for i in c:
    print(f"{i[0]}{i[1]}{i[2]}{i[3]}")