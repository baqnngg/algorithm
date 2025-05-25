#약수들의 합
while 1:
    a = int(input())
    if a == -1:
        break
    m = []
    for i in range(1,int(a/2)+1):
        if a%i == 0:
            m.append(i)
    if sum(m) == a:
        print(f"{a} =",end=" ")
        for i in range(len(m)-1):
            print(f"{m[i]} +",end=" ")
        print(f"{m[-1]}")
    else:
        print(f"{a} is NOT perfect.")