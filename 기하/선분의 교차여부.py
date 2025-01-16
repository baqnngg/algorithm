# x1,y1,x2,y2 = map(int,input().split())
# x3,y3,x4,y4 = map(int,input().split())
# ccw1 = (x1*y2)+(x2*y3)+(x3*y1) - ((x2*y1)+(x3*y2)+(x1*y3))
# ccw2 = (x1*y2)+(x2*y4)+(x4*y1) - ((x2*y1)+(x4*y2)+(x1*y4))
# ccw3 = (x3*y4)+(x4*y1)+(x1*y3) - ((x4*y3)+(x1*y4)+(x3*y1))
# ccw4 = (x3*y4)+(x4*y2)+(x2*y3) - ((x4*y3)+(x2*y4)+(x3*y2))
# if ccw1*ccw2 == 0 or ccw3*ccw4 == 0:
#     if max(x1,x2) < min(x3,x4) or min(x1,x2) > max(x3,x4):
#         print(0)
#     elif max(y1,y2) < min(y3,y4) or min(y1,y2) > max(y3,y4):
#         print(0)
#     else:
#         print(1)
# elif ccw1*ccw2 <= 0 and ccw3*ccw4 <= 0:
#     print(1)
# else:
#     print(0)
# 조건 같은거

import sys
input = sys.stdin.readline
# [1] 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# CCW 함수
def ccw(x1, y1, x2, y2, x3, y3):
    result = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if result >0: # 양수면 반시계 방향
        return 1
    elif result <0: # 음수면 시계 방향
        return -1
    elif result == 0: # 0이면 일직선
        return 0
# 일직선의 경우 선분의 겹침 여부 판별 함수
def is_overlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
        return True
    else:
        return False

# 선분의 교차 여부 판별 함수
def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw_abc = ccw(x1, y1, x2, y2, x3, y3)
    ccw_abd = ccw(x1, y1, x2, y2, x4, y4)
    ccw_cda = ccw(x3, y3, x4, y4, x1, y1)
    ccw_cdb = ccw(x3, y3, x4, y4, x2, y2)
 
 # [2] 선분 교차 여부 판별하기   
    if ccw_abc * ccw_abd == 0 and ccw_cda * ccw_cdb == 0: # 두 선분이 일직선인 경우
        return is_overlab(x1, y1, x2, y2, x3, y3, x4, y4) # 일직선의 경우 선분의 겹침 여부 판별
    elif ccw_abc * ccw_abd <=0 and ccw_cda * ccw_cdb <= 0: # 두 선분이 교차하는 경우
        return True
    else: # 두 선분이 겹치지 않는 경우
        return False

result_cross = is_cross(x1, y1, x2, y2, x3, y3, x4, y4)

# [3] 정답 출력
if result_cross == True:
    print(1)
else:
    print(0)