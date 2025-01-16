def solution(temperatures):
    answer = 0
    for temperature in temperatures:
        if temperature[0] <= -15 and temperature[1] <= -5:
            answer += 2000
        else:
            answer += 500

    return answer
 # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
temperatures = [[0, 5], [-15, -5], [-16, -3], [-20, -8], [-14, -6]]
ret = solution(temperatures)
 # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")