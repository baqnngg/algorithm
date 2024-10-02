n = int(input())
for i in range(n):
    a = input()
    sum_n = 0
    ii = 0
    for j in a:
        if j == "O":
            ii+=1
            sum_n+=ii
        else:
            ii = 0
    print(sum_n)