#삼각형과 세 변
a,b,c = 1,1,1
while 1:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0: break
    elif max(a,b,c) >= ((a+b+c)-max(a,b,c)): print("Invalid")
    elif a == b and b == c and c == a: print("Equilateral")
    elif a == b or b == c or c == a: print("Isosceles")
    elif a != b and b != c and c != a: print("Scalene")