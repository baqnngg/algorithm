import  sys
input = sys.stdin.readline
a = int(input())
d = {}
for _ in range(a):
    b,c = input().split('.')
    if c[:len(c)-1] in d:
        d[c[:len(c)-1]] += 1
    else:
        d[c[:len(c)-1]] = 1
d = sorted(d.items(), key=lambda x:x[0])
for i in d:
    print(i[0],i[1])