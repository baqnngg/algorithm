# 라디안 기억, 시분초 거리 계산 같은거 각도도 기억
# 특히 제일중요한거 math 함수에서 cos과 sin쓸수있다는거
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=
import math

h,m,s = map(int,input().split(':'))
second_angle = 6 * s
minute_angle = 6 * m
hour_angle = 30 * (h % 12) + 0.5 * m

time = [hour_angle, minute_angle, second_angle]
length = [120,200,180]

for i in range(3):
    radians = math.radians(time[i])
    x = length[i] * math.cos(radians)
    y = length[i] * math.sin(radians)
    x,y = round(x), round(y)
    print(f"({int(y)}, {int(x)})")