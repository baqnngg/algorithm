#소수 찾기
x = int(input())
cnt = 0
for x in list(map(int,input().split())):
    for i in range(2,x+1):      
        if x % i == 0:  
            if x == i:
                cnt += 1
            break
print(cnt)