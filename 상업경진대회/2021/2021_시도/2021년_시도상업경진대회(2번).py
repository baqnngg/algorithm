n = int(input())
for _ in range(n):
    a = input()
    ss = 0
    k = 2

    for i in range(len(a)):
        if a[i] == "-": continue
        if i == 13: break
        if k == 10: k = 2
        ss += int(a[i]) * k
        k += 1

    ss = int(ss%11)
    ss = 11 - ss
    if ss == 10: ss = 0
    elif ss == 11: ss = 1

    if ss == int(a[-1]): print(ss,"O")
    else: print(ss,"X")