n = int(input())
# 개미집의 각방의 상태 저장
di = list(map(int,input().split()))
# 1부터 쓰기위해 0번째 노드에 0넣음
di.insert(0,0)
# 어디로 가는지 저장
nav = list(map(int,input().split()))
# 어디굴에 있는지 찾는 초기값
cc = 1
for i in range(len((nav))):
    # 왼쪽으로 가는 경우
    if nav[i] == 0:
        # 방이 없으면 cc에 지금있는 방 저장 break
        if di[cc*2] == 0:
            cc = cc
            break
        else:
            cc = cc*2
    # 오른쪽으로 가는 경우
    else:
        # 방이 없으면 cc에 지금있는 방 저장 break
        if di[(cc*2)+1] == 0:
            cc = cc
            break
        else:
            cc = (cc*2)+1
# 정답출력
print(cc)