# 4번 -------------- ord, chr 중요
a = input()
b = input()
for i in b:
    c = ord(i)-ord('a')
    if c < 0:
        print(" ",end="")
    else:
        print(a[c],end="")