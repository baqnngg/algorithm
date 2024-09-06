# 1 : AI 혁신 공모전
# a = int(input())
# # 대상
# if a <= 1: print(100000000)
# # 햑신 + 최우
# elif a <= 2: print(35000000)
# # 최우
# elif a <= 5: print(30000000)
# # 우수
# elif a <= 10: print(10000000)
# # 장려
# elif a <= 20: print(1000000)
# else: print(0)

# 2 : 마법의 문 열기
# a = input()
# print(a,a,a)

# 3 : 칵테일 사랑
a = int(input())
b = list(map(int, input().split()))
cnt = 0
for i in range(a-1, 0, -1):
    for j in range(i):
        if b[j] > b[j + 1]:
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp
            cnt += 1
print(cnt)