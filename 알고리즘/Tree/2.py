import sys
input = sys.stdin.readline
 # [1] 입력 받기
n = int(input())
tree = {}  # 딕셔너리 형태로 선언
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
 # 전위 순회 함수
def pre_order(now):
    if now == '.':
        return
    print(now, end='')  # 1.현재 노드
    pre_order(tree[now][0])  # 2.왼쪽 탐색
    pre_order(tree[now][1])  # 3.오른쪽 탐색
# 중위 순회 함수
def in_order(now):
    if now == '.':
        return
    in_order(tree[now][0])  # 1.왼쪽 탐색
    print(now, end='')  # 2.현재 노드
    in_order(tree[now][1])  # 3.오른쪽 탐색
# 후위 순회 함수
def post_order(now):
    if now == '.':
        return
    post_order(tree[now][0])  # 1.왼쪽 탐색
    post_order(tree[now][1])  # 2.오른쪽 탐색
    print(now, end='')  # 3.현재 노드
# [2] 순회 함수 실행
pre_order('A') # 전위 순회 함수 호출
print()
in_order('A') # 중위 순회 함수 호출
print()
post_order('A') # 후위 순회 함수 호출