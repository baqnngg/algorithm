from itertools import combinations
import copy
n,k,l = map(int,input().split())
box = list(map(int,input().split()))
m = []
summ = []
for i in combinations(box, k):
    box1 = copy.deepcopy(box)
    i = list(i)
    i.sort()
    kk = i[1]
    m.append(kk)
    for j in range(len(box1)):
        if kk >= box[j]:
            box1[j] = 0
    summ.append(sum(box1))
print(max(summ)-m[summ.index(max(summ))])