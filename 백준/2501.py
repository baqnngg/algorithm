#약수 구하기
n,k = map(int,input().split())
b = []
for i in range(1,n+1):
    if n%i == 0:
        b.append(i)

if len(b) < k:
    print(0)
else:
    print(b[k-1])