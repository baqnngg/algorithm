import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m,k = map(int,input().split())

tree_height = 0
length = n

while length != 0:
    length //= 2
    tree_height += 1

tree_size = pow(2, tree_height + 1) 

left_node_start_index = (tree_size // 2) - 1
tree = [1] * (tree_size+1)

for i in range(left_node_start_index+1,left_node_start_index+n+1):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        tree[i//2] = (tree[i//2] * tree[i])%1000000007
        i -= 1

def change_value(index):
    if index <= 0:
        return
    tree[index] = (tree[index*2]*tree[(index*2)+1])%1000000007
    change_value(index//2)

def get_sum(s,e):
    part_sum = 1
    # 탐색종료 조건
    while s <= e:
        if s % 2 == 1:
            part_sum = (part_sum * tree[s])%1000000007
            s += 1
        if e % 2 == 0:
            part_sum = (part_sum * tree[e])%1000000007
            e -= 1
        # 부모 노드로 이동
        s = s//2
        e = e//2
    return part_sum

set_tree(tree_size-1) #초기 트리 생성

for _ in range(m+k):
    question, s, e = map(int,input().split())
    if question == 1:
        tree[left_node_start_index+s] = e
        change_value((left_node_start_index+s)//2)
    elif question == 2:
        s = s + left_node_start_index
        e = e + left_node_start_index
        print(get_sum(s,e))