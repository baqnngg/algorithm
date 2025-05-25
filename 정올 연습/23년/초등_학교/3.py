# 개미는 어디있을까
d = int(input())
m = 1
room = list(map(int, input().split()))
move = list(map(int, input().split()))

for i in range(len(move)):
    if move[i] == 0:
        if len(room) < (m*2): break
        if room[(m*2)-1] == 0: break
        m *= 2
    elif move[i] == 1:
        if len(room) < ((m*2)+1): break
        if room[(m*2)] == 0: break
        m = (m * 2) + 1
print(m)