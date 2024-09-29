a,b,c = map(int,input().split())
money = a-b
kk = 0
p = True

if 12000000 <= money: kk += 12000000 * 0.06
else:
    if p:
        kk += money * 0.06
        p = False

if 46000000 <= money: kk += (46000000-12000000)*0.15
else:
    if p:
        kk += (money-12000000)*0.15
        p = False

if 88000000 <= money: kk += (88000000-46000000)*0.24
else:
    if p:
        kk += (money-46000000)*0.24
        p = False

if 150000000 <= money: kk += (150000000-88000000)*0.35
else:
    if p:
        kk += (money-88000000)*0.35
        p = False

if 300000000 <= money: kk += (300000000-150000000)*0.38
else:
    if p:
        kk += (money-150000000)*0.38
        p = False

if 500000000 <= money: kk += (500000000-300000000)*0.4
else:
    if p:
        kk += (money-300000000)*0.4
        p = False

if 500000000 < money: kk += (money-500000000)*0.42

if int(kk-c) <= 0: print(0)
else:
    if str(int(kk-c))[-1] == "0":
        print(int(kk-c))
    else:
        cc = list(str(int(kk-c)))
        cc[-1] = "0"
        for i in cc:
            print(i,end="")