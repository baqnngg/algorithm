n = int(input())
O = [0,0]
z = [list(map(int,input().split())) for _ in range(n)]
z.append(z[0])

ans = 0

for i in range(n):
    ans += ((O[0]*z[i][1]) + (z[i][0]*z[i+1][1]) + (z[i][0]*O[1]))-((z[i][0]*O[1]) + (z[i+1][0]*z[i][1]) + (O[0]*z[i+1][1]))

print(abs(ans)/2)