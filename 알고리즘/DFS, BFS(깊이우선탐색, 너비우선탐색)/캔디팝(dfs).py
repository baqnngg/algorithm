cnt_color = 0
cnt_crush = 0
graph = []

def dfs(candy,x, y):
    global cnt_color
    if x < 0 or x > 6 or y < 0 or y > 6:
        return
    
    if graph[x][y] == candy:
        cnt_color+=1  
        graph[x][y] = 0   
        dfs(candy, x-1, y) 
        dfs(candy, x, y-1) 
        dfs(candy, x+1, y) 
        dfs(candy, x, y+1) 
        return
    
    return 

for i in range(7):
        graph.append(list(map(int, input().split())))
        
for i in range(7):
    for j in range(7):
        if graph[i][j] != 0:
          dfs(graph[i][j] ,i, j)
          if cnt_color >=3:
             cnt_crush+=1 
          cnt_color = 0 
    
print(cnt_crush)
