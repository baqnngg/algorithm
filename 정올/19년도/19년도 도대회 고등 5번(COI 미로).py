n = int(input())
cn = 0
move = 0
maze = list(map(int,input().split()))
maze.insert(0,0)
visited = [0] * (n+2)
visited[1] = 1
i = 1
while 1:
    if visited[i] % 2 == 0:
        i += 1
        move += 1
        visited[i] += 1
    else:
        move += 1
        i = maze[i]
        visited[i] += 1
    
    if visited[n+1] >= 1:
        break

# 출력
print(move)