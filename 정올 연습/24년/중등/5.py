# 탁자
import sys
import math

# [1] 첫 줄 입력 받기: n은 배열의 크기, m은 질의 개수
n, m = map(int, input().split())

arr = []  # 정수들을 저장할 리스트

# [2] n개의 정수를 입력받아 arr에 저장
for i in range(n):
    a = int(input())
    arr.append(a)

# [3] m개의 질의에 대해 각각 처리
for i in range(m):
    a = int(input())  # 현재 질의 값 (기준값)
    
    res_min, res_max = 0, 10**18  # 최소값과 최대값 초기화 (최대 범위로 설정)

    # [4] arr에서 4개를 고르는 모든 조합을 완전 탐색
    for j in range(n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for o in range(l+1, n):
                    # 선택한 네 수의 최소공배수(LCM)를 구함
                    g1 = math.gcd(arr[j], arr[k])
                    multiple = arr[j] * arr[k] // g1  # j와 k의 LCM

                    g2 = math.gcd(multiple, arr[l])
                    multiple = multiple * arr[l] // g2  # j, k, l의 LCM

                    g3 = math.gcd(multiple, arr[o])
                    multiple = multiple * arr[o] // g3  # j, k, l, o의 LCM

                    # [5] a 이하이면서 가장 큰 multiple의 배수를 구함 (최솟값 후보)
                    res_min = max(res_min, multiple * (a // multiple))

                    # [6] a 이상이면서 가장 작은 multiple의 배수를 구함 (최댓값 후보)
                    res_max = min(res_max, multiple * ((a + multiple - 1) // multiple))

    # [7] 각 질의에 대한 결과 출력
    print(res_min, res_max)
