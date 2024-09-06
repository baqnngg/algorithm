import sys
input = sys.stdin.readline
# [1] 입력 받기
n = int(input())
m = int(input())

material = list(map(int, input().split()))

# [2] 만들수 있는 갑옷 개수 구하기(투포인터)
material.sort()
start_index = 0
end_index = n-1
cnt = 0
sum = 0
while start_index < end_index:
    if material[start_index] + material[end_index] == m:
        cnt += 1
        start_index += 1
        end_index -= 1
    elif material[start_index] + material[end_index] < m:
        start_index += 1
    elif material[start_index] + material[end_index] > m:
        end_index -= 1

# [3] 정답 출력
print(cnt)