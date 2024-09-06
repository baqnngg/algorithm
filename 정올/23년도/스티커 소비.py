n = int(input())
k = list(map(int,input().split()))
a,b = map(int,input().split())
st = []
day = []
for i in range(a-1,b):
    st.append(k[i])
    day.append(1)

while st.count(0) != len(st):  
    odd_num = []
    for i in range(len(st)):
        if st[i] % 2 == 0:
            continue
        else:
            odd_num.append(st[i])

    for i in range(len(st)):
        if st[i] == 0:
            continue
        if st[i] % 2 == 0:
            st[i] = int(st[i] / 2)
            day[i] += 1
        else:
            st[i] = min(odd_num) - 1
            day[i] += 1
            
print(*day)