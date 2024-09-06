N = int(input())
factory = list(map(int,input().split()))
money = []
for i in range(100):
    factory.append(0)

while max(factory) != 0:
    for i in range(N):
        if factory[i] != 0 and factory[i+1] != 0 and factory[i+2] != 0:
            factory[i],factory[i+1],factory[i+2] = factory[i]-1,factory[i+1]-1,factory[i+2]-1
            money += 7
        elif factory[i] != 0 and factory[i+1] != 0:
            factory[i],factory[i+1] = factory[i]-1,factory[i+1]-1
            money += 5
        elif factory[i] != 0:
            factory[i] = factory[i] - 1
            money += 3

print(min(money))