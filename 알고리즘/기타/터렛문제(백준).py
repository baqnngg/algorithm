import math

#설계1 : 입력받기
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

#설계2 : 원의 방정식으로 어떤점에서 만나는지 알기위해 원의방정식 활용
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 원의방정식을 활용
               #(x - a)**2 + (y - b)**2 = r**2 : 원의 방정식
#설계3 : 판단, 출력
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때(무한대)
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때(1점에서 만날때)
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)