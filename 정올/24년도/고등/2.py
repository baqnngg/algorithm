a = input()
b = []
for i in a:
    if ord(i) >= 97 and ord(i) <= 122:
        b.append(ord(i))
print(max(b)-min(b))