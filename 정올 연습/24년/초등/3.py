# 파스칼의 삼각형
n = int(input())
pas = [[1],[1,1]]
for i in range(2,n):
    pas.append([1]*(i+1))
    for j in range(1,i):
        pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
for i in range(n):
    print(*pas[i])