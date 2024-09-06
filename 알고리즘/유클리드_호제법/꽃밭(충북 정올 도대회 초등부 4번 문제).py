#[설계3] 서로소 판별
def co_p(x, y):
    #유클리드 호제법
    x = abs(x)
    y = abs(y)
    if x < y: x, y = y, x

    while y != 0:
        x, y = y, x % y

    if x == 1: #서로소 판별
        return 1 #참
    else:
        return 0 #거짓

# init
inp = []
#[설계1] 꽃밭
N, M = map(int, input().split())
T = int(input())
for idx in range(T):
    x, y = map(int, input().split())
    inp.append([x, y])

# bruth-force
MOD = 10007
for i in range(T):
    cnt = 0

    # 3개의 점 구하기
    p = []
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            #말뚝 연결가능한지 [설계2] -- 서로소 판별(유클리드 호제법)
            if co_p(x - inp[i][0], y - inp[i][1]): 
                p.append([x, y])

    l = len(p)
    #[설계4] 연결가능 판별  
    for i in range(l):
        for j in range(i + 1, l):
            if co_p(p[i][0] - p[j][0], p[i][1] - p[j][1]): 
                cnt = (cnt + 1) % MOD #꽃밭개수 세기

    # [설계5]출력
    print(cnt)  