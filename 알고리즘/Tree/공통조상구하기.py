import sys
# [1] 트리 입력 받기
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(0, N-1): # 인접 리스트에 트리 데이터 저장
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
depth = [0]*(N+1)
parent = [0]*(N+1)
visited = [False]*(N+1)
# 부모 노드, 깊이 구하기 함수(BFS)
def BFS(node):
    queue = [node]
    visited[node] = True
    while queue:
        now_node = queue.pop(0)
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node # 부모 노드 저장
                depth[next] = depth[now_node]+1 # 노드 depth 저장
# [2] 부모 노드, 깊이 구하기 함수 호출(BFS)
BFS(1)
def excute_lca(a, b):
    if depth[a] < depth[b]: # 깊은 값을 앞에 두기
        temp = a
        a = b
        b = temp
    while depth[a] != depth[b]: # depth 맞추기
        a = parent[a]
    while a != b: # 공통 조상 찾기
        a = parent[a]
        b = parent[b]
    return a # 공통 조상 반환
# [3] 최소 공통 조상 구하기(LCA)
M = int(input())
mydict = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if not mydict.get((a, b), 0): 
        mydict[(a, b)] = mydict[(b, a)] = excute_lca(a, b)
    print(mydict.get((a, b))) # 공통 조상 출력