from collections import deque
import sys
input = sys.stdin.readline

# [설계1] 입력 받기
n, m, q, k = map(int, input().split()) 
# n: 봉화 지역의 수, m: 인접한 지역 정보, q: 외계인 침략이 일어난 봉화의 수, k: 첫날 소식을 전달하는 거리
arr = [-1] * (n + 1) # 침략지로부터 떨어진 봉화의 거리 정보 저장 
# ex) arr[2]가 2인 경우: 2번 봉화까지 거리가 2임.
darr = [0] * (2 * n + 1) # 소식 전달 받기까지 걸린 일수 저장
# ex) darr[2]가 2인 경우: 거리가 2인 곳까지 소식 전달되기까지 2일 걸림.
adj_list = [[] for _ in range(n + 1)] # 인접 리스트
queue = deque()

temp_q = list(map(int, input().split()))
for i in range(q):
    arr[temp_q[i]] = 0
    queue.append(temp_q[i])

# 인접 리스트 만들기
for _ in range(m):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

# [설계2] 침략지로부터 떨어진 봉화 거리 저장하는 리스트 만들기(BFS)
while queue:
    a = queue.popleft()
    for s in adj_list[a]:
        if arr[s] == -1:
            arr[s] = arr[a] + 1
            queue.append(s)

# [설계3] 침략 소식 전달받기까지 걸리는 일수를 저장하는 리스트 만들기
sum = 0 
day = 0
while sum <= n:
    day += 1
    start = sum + 1
    sum = min(n + 1, sum + day * k)
    for i in range(start, sum + 1):
        darr[i] = day
        
# [설계4] 정답 출력
for i in range(1, n + 1):
    print(darr[arr[i]], end=" ")