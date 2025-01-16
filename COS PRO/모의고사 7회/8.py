# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(best):
    # 여기에 코드를 작성해주세요.
    answer = 0
    b = ["a","b","c","d","e"]
    cc = 0
    while best:
        for i in b:
            if i in best:
                cc += 1
                best.remove(i)
        if cc == 5:
            answer+=1
            cc = 0
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
best = ["e", "c", "b", "b", "a", "d", "a"]
ret = solution(best)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")