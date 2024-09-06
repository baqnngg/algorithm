a,b,c = map(int,input().split())
if a >= 10:
    a = (a*500)*0.9
else:
    a = a*500
if b >= 15:
    b = (b*800)*0.85
else:
    b = b*800

print(int(a+b+(c*1000))) 