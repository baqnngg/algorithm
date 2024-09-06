a = input()
b = 0
for i in a:
    if ord(i)-3 < 65:
        b = ord(i)-3 + 26
        print(chr(b),end="")
    else: 
        print(chr(ord(i)-3),end="")