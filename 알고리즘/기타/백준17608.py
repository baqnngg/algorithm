n = int(input())
h = [int(input()) for _ in range(n)]
cnt = 1
h = list(reversed(h))
k = h[0]
for i in range(1,n):
    if h[i] > k:
        k = h[i]
        cnt += 1
print(cnt)