# 1 : 비밀 요원의 숫자 비교 임무
# a,b = map(int,input().split())
# if a == b: 
#     print("safe")
# else: 
#     print("warning")

# 2 : 1등과 꼴찌
# a = int(input())
# b = list(map(int,input().split()))
# print(max(b))
# print(min(b))

# 3 : 카드놀이
# a = int(input())
# c = []
# b = [c.append(i) for i in range(1,a+1)]
# while len(c) != 1:
#     d = c[0]
#     c.remove(d)
#     c.append(d)
#     c.remove(c[0])
# print(c[0])

# 4 : 경품
# a = int(input())
# b = list(map(int,input().split()))
# c = set(b)
# print(len(b)-len(c))