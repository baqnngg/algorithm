a = list(input().split())
ss = 0

for i in a:
    if len(i) == 4:
        for j in range(len(i)):
            if j == 0 or j == 2:
                aa = int(i[j]) * 2
                if len(str(aa)) == 1:
                    ss += aa
                else:
                    ss += sum([int(k) for k in list(str(aa))])                        
            else:
                ss += int(i[j])
    else:
        print(-1)
        exit()

if a[0][0:2] == "35": print("JCB", end=" ")
elif a[0][0:2] == "37": print("American Express",end=" ")
elif a[0][0] == "4": print("VISA",end=" ")
elif a[0][0:2] == "51" or a[0][0:2] == "52" or a[0][0:2] == "53" or a[0][0:2] == "54" or a[0][0:2] == "55": print("MasterCard",end=" ")
elif a[0][0:2] == "65": print("BC Global",end=" ")
elif a[0][0] == "9": print("Local",end=" ")

else:
    print(-2)
    exit()
if ss % 10 == 0:
    print(ss,"O")
else:
    print(ss,"X")