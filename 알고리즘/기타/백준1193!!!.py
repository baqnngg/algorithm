# 대각선 아이디어, 짝수 홀수에 따른 계산 =======================================
X = int(input())
# 대각선의 번호
diagonal = 1

# X가 속한 대각선을 찾음
while X > diagonal:
    X -= diagonal
    diagonal += 1

# 대각선의 번호에 따라 분수 계산
if diagonal % 2 == 0:
    numerator = X
    denominator = diagonal - X + 1
else:
    numerator = diagonal - X + 1
    denominator = X

print(f"{numerator}/{denominator}")


# 이건 도대체 뭐가 틀린건지 모르겠네
# n = int(input())
# i = 1
# ss = 1
# # if n >= 5000000:
# #     n = 10000000-n
# # if n == 0:
# #     print(f"{0}/{1}")
# #     exit()
# while 1:
#     i += 4   #증가치
#     ss += i  # 총 몇개인지는 구함
#     if ss > n-1:
#         if n-(ss-i) > int(i/2)+1: #만약에 제일 큰값보다 크면 -1 해줘 야되는데
#             print(f"{(int(i/2)+1)-((n-(ss-i))-(int(i/2)+1))}/{(n-(ss-i))-int(i/2)}")
#         else:
#             if (int(i/2)+1)-(n-(ss-i)) == 0:
#                 print(f"{n-(ss-i)}/1")
#             else:
#                 print(f"{n-(ss-i)}/{(int(i/2)+1)-(n-(ss-i))}")
#         break