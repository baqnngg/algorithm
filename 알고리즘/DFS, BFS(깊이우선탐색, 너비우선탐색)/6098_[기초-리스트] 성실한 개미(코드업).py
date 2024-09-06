house = []
for i in range(10):
    house.append(list(map(int,input().split())))
def move(x,y):
    global house
    
    #개미가 오른쪽에 길이 있거나 젤리가 있으면 
    if house[x][y+1] == 0 or house[x][y+1] == 2:
        #젤리면 이거실행
        if house[x][y+1] == 2:
            house[x][y+1] = 9
            return #종료시킴
        #길이면 이거 
        house[x][y+1] = 9
        move(x,y+1) #오른쪽으로 갔으니까 저장
    
    #오른쪽이 막혀있으면 ㄱㄱ
    elif house[x][y+1] == 1:
        #젤리 있으면 이거 실행
        if house[x+1][y] == 2:
            house[x+1][y] = 9
            return
        
        # 오른쪽도 못가고 아래도 못가니까 종료
        elif house[x+1][y] == 1:
            return
        
        #길이면 이거 실행
        house[x+1][y] = 9
        move(x+1,y)

move(1,0)

for i in range(10):
    print(*house[i])