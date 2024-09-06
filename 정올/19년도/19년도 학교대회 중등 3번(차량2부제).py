a = int(input())
car = list(map(int,input().split()))
cnt = 0
if a % 2 == 0:
    for i in car:
        if i % 2 == 0:
            cnt += 1 
else:
    for i in car:
        if i%2 != 0:
            cnt += 1
print(cnt)