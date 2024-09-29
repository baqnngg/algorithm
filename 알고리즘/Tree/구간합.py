import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

tree_height = 0
length = n

while length != 0:
    length //= 2
    tree_height += 1

tree_size = pow(2, tree_height + 1) 

left_node_start_index = (tree_size // 2) - 1
tree = [0] * (tree_size+1)

for i in range(left_node_start_index+1,left_node_start_index+n+1):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

def change_value(index,value):
    difference = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + difference
        index //= 2

def get_sum(s,e):
    part_sum = 0
    # 탐색종료 조건
    while s <= e:
        if s % 2 == 1:
            part_sum += tree[s]
            s += 1
        if e % 2 == 0:
            part_sum += tree[e]
            e -= 1
        # 부모 노드로 이동
        s = s//2
        e = e//2
    return part_sum

set_tree(tree_size-1) #초기 트리 생성

for _ in range(m+k):
    question, s, e = map(int,input().split())
    if question == 1:
        change_value(left_node_start_index+s,e)
    elif question == 2:
        s = s + left_node_start_index
        e = e + left_node_start_index
        print(get_sum(s,e))