# c,v,t,k,d = map(int,input().split())
# #c 인간 속력,  v는 호랑 속력, t는 인간 발견하는 시간, k는 호랑이가 떡먹고 입구로 돌아감, d는 거리
# rc = 0 #떡 개수
# cd = 0 
# vd = 0 #사람 거리 변수, 호랑이 거리 변수 초기화
# time = 0
# time2 = 0-t
# cc = []
# # (1) 호랑이가 따라왔을때까지 충북이가 이동한 위치
# # (2) 호랑이가 돌아갔을 때, 충북이가 이동한 위치
# # (3) 호랑이가 쉬는 동안 충북이가 이동한 위치   
# while cd != d:
#     #시간 + 1 
#     time += 1
#     time2 += 1

#     #거리 구하고있음
#     cd = c * time
#     vd = v * time2

#     #인간의 거리가 거리를 넘어갔거나 같을때
#     if cd >= d:
#         break
    
#     # 사람과 호랑이 거리가 같거나 작을때
#     if cd <= vd:
#         time2 = 0-(k+t)
#         rc += 1
#         cc.append(cd)

# print(rc)


# 쌤코드
import sys
input = sys.stdin.readline
# [설계1] 입력 받기
vc, vt, t, k, d = map(int, input().split())
# vc: 충북이 속도, vt: 호랑이 속도, t: 호랑이가 사람 냄새를 알게된 시간
# k: 호랑이가 떡을 먹고 박달재 입구로 돌아간 후 쉬는 시간, d: 박달재 입구부터 출구까지 거리
pos = t * vc # 호랑이가 사람 인식하기 전까지 충북이가 이동한 위치
rice_cake = 0

# [설계2] 충북이 위치, 떡 계산하기
while (d-pos)/vc > d/vt:
# 충북이가 목적지까지 가는데 필요한 시간 > 호랑이가 목적지까지 가는데 필요한 시간
    pos += (pos / (vt - vc)) * vc # (1) 호랑이가 따라왔을때까지 충북이가 이동한 위치
    rice_cake += 1 # 호랑이가 따라왔을 때 떡 1개 제공
    pos += (pos / vt) * vc # (2) 호랑이가 돌아갔을 때, 충북이가 이동한 위치
    pos += k * vc # (3) 호랑이가 쉬는 동안 충북이가 이동한 위치    
    
# [설계3] 정답 출력    
print(rice_cake)