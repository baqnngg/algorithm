a = int(input())
b = int(input())
c = sum(list(map(int,input().split())))
if a >= c:
    print("YES")
else:
    print("NO")