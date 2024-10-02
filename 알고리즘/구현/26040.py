a = list(input())
b = list(input().split())
for i in a:
    if i in b: print(str(i.lower()),end="")
    else: print(i,end="")