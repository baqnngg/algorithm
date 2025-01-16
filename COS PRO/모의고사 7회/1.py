def solution(grid):
    answer = []
    for i in range(1, 6):
        if i%2 == 1:
            answer.append(max(grid[i-1]))
        else:
            answer.append(min(grid[i-1]))
    return answer
 # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
grid = [[20, 8, 29, 4, 3], [10, 26, 28, 49, 27], [45, 5, 19, 38, 25], [9, 31, 36, 11, 35], [12, 40, 24, 33, 6]]
ret = solution(grid)
 # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")