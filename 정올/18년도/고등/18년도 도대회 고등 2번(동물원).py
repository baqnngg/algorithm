# 내꺼
# from collections import deque
# def ec(x,y):
#     global queue
#     ctt = 0
#     x, y = x,y
#     for i in range(4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]
#         if graph[next_x][next_y] == "P":
#             ctt += 1
#     gg.append((ctt,x,y))

# def ec2():
#     global cnt
#     queue = deque(gg)
#     while queue:
#         cc, x, y = queue.popleft()
#         for i in range(4):
#             next_x = x + dx[i]
#             next_y = y + dy[i]
#             if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
#                 continue
#             if graph[next_x][next_y] == "P":
#                 graph[next_x][next_y] = "W"
#                 graph[x][y] = "0"
#                 cnt += 1
#                 break

# # 입력받기
# m, n = map(int,input().split())
# graph = [list(input()) for _ in range(m)]
# cnt = 0
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# gg = []
# # W근처에 P가 얼마나 있는지 구함
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == "W":
#             ec(i,j)
# # W근처에 P가 적은 것 부터 돌림
# gg.sort()
# ec2()
# # 정답출력
# print(cnt)

# 쌤꺼 #######################################################################
# [설계1] 입력 받기
n, m = map(int, input().split())
cnt_pig = 0 # 잡아먹힌 돼지수
dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1 ,1]
graph = []
for i in range(n):
        graph.append(list(input()))
# [설계2] 돼지를 기준으로 상,하,좌,우 탐색하기
for i in range(n):
    for j in range(m):
          if graph[i][j] == 'P':
              for k in range(4):
                  if 0 <= i + dx[k] < n and 0 <= j + dy[k] < m:
                      if graph[i+dx[k]][j+dy[k]] == 'W':
                        graph[i+dx[k]][j+dy[k]] = '.'
                        graph[i][j] = '.'
                        cnt_pig+=1 
                        break
# [설계3] 정답 출력
print(cnt_pig)