a,b = map(int,input().split())
m = a*60+b
j = sum(list(map(int,input().split())))
m -= j
print(m//60,m%60)