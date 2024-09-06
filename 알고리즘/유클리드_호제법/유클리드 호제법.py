x,y = map(int,input().split())
while y != 0:
    r = x % y
    x = y
    y = r
print(x)

###함수버전
def a(x,y):
    if x < y:
        x,y = y,x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

print(a(x,y))