import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(start):
    stack = [start]
    color[start] = 1  # 시작 노드 색상 지정

    while stack:
        v = stack.pop()
        for neighbor in adj_list[v]:
            if color[neighbor] == 0:  # 아직 색칠하지 않은 경우
                color[neighbor] = 3 - color[v]  # 현재 색과 다른 색으로 칠함
                stack.append(neighbor)
            elif color[neighbor] == color[v]:  # 같은 색이면 이분 그래프 아님
                return False
    return True

n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)  # 0: 미방문, 1: 색상1, 2: 색상2

    for _ in range(e):
        s, g = map(int, input().split())
        adj_list[s].append(g)
        adj_list[g].append(s)

    ans = 'YES'
    for i in range(1, v + 1):
        if color[i] == 0:  # 아직 방문하지 않은 정점
            if not dfs(i):  # DFS 호출
                ans = 'NO'
                break

    print(ans)
