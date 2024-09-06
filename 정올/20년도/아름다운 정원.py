gr = [list(input()) for i in range(4)]
ans = "NO"
for i in range(3):
    for j in range(3):
        kk = gr[i][j]+gr[i][j+1]+gr[i+1][j]+gr[i+1][j+1]
        if kk.count("#") >= 3:
            ans = "YES"
        elif kk.count(".") >= 3:
            ans = "YES"
print(ans)