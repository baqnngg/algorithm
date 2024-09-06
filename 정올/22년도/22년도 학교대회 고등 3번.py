a,b,c = map(int,input().split())
if a == 0:
    if b == 0:
        if c == 0:
            print("간장 고기 볶음면")
        else:
            print("간장 고기 우동")
    else:
        if c == 0:
            print("간장 감자 조림")
        else:
            print("간장 감자 찌개")
else:
    if b == 0:
        if c == 0:
            print("매운 고기 볶음면")
        else:
            print("매운 고기 우동")
    else:
        if c == 0:
            print("매운 감자 조림")
        else:
            print("매운 감자 찌개")