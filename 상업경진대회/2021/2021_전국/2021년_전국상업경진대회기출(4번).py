# '완전 탈착(Derangement)' 문제는 주어진 n개의 요소에서 아무도 자신의 원래 자리를 차지하지 않도록 배치하는 경우의 수를 구하는 문제입니다.
# D(n) = (n - 1) * (D(n - 1) + D(n - 2))
# =\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\\=\=\=\=\=

a = int(input())
if a == 0: 
    print(0)
    exit()
if a == 2:
    print(1)
    exit()
if a < 1 or a > 20:
    print("오류")
    exit()

derangements = [0] * (a + 1)
derangements[1] = 0
derangements[2] = 1
for i in range(3, a + 1):
    derangements[i] = (i - 1) * (derangements[i - 1] + derangements[i - 2])

print(derangements[a])