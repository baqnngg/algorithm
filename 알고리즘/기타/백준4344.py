c = int(input())
for _ in range(c):
    n = list(map(int, input().split()))
    n.pop(0)
    l = sum(n) / len(n)
    p = 0
    for i in n:
        if l < i:
            p += 1
    dd = (p/len(n))*100
    print("%.3f%%" %(dd))