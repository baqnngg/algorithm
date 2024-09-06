import sys
a = int(sys.stdin.readline())
player = []
player = [list(map(int,input().split())) for i in range(a)]
cnt = []
cnt = sorted([int(player[i][1]) for i in range(a)],reverse=True)

for i in range(a):
    # 무게마다 무게만따져서 최대로 얻을수있는 무게
    total = sum(cnt) - sum(cnt[0:i+1])
    color = []
    for k in range(a):
        if cnt[i] == player[k][1]:
            colornum = k
    # 여기에서 같은 색깔(자신을 제외한)의 위치 저장
    for k in range(a):
        if player[colornum][0] == player[k][0] and colornum != k:
            color.append(k) 
    
    if color == []:
        player[colornum].append(total)
    else:
        for j in range(len((color))):
            total -= player[color[j]][1]
        if total < 0:
            total = 0
        player[colornum].append(total) 
# 출력
for i in range(a):
    print(player[i][2])