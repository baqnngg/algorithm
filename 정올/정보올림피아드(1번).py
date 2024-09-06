from itertools import permutations
n,d = map(int,input().split())
arr = list(map(int,input().split()))
possible = []
for i in permutations(arr, 2):
    if abs(i[0]-i[1]) <= d or abs(i[1]-i[0]) <= d:
        possible.append(i)

print(len(possible))