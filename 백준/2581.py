#소수
n = int(input())
m = int(input())
s = []
cc = True
for i in range(n,m+1): 
    if i > 1 :    
        for j in range(2, i): 
            if i % j == 0:  
                cc = False
                break
        if cc == True:
            s.append(i)
        else:
            cc = True

if s == []:
    print(-1)
else:
    print(sum(s))
    print(min(s))