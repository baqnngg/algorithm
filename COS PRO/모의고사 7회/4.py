def func_a(arr):
    ret = []
    for a in arr:
        start_time = func_b(a[0])
        end_time = func_b(a[1])
        ret.append(end_time-start_time) #
    return ret

def func_b(s):
    hour = int(s[0]) * 10 + int(s[1]) #
    minute = int(s[3]) * 10 + int(s[4]) #
    second = int(s[6]) * 10 + int(s[7]) #
    return hour * 3600 + minute * 60 + second

def func_c(arr):
    min_num = min(arr)
    for i, a in enumerate(arr):
        if min_num == a:
            return min_num

def solution(times):
    records = func_a(times)
    answer = func_c(records)
    return answer

 # 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
times = [["22:10:05", "22:10:08"], ["22:10:28", "22:10:30"], ["23:10:10", "23:10:12"]]
ret = solution(times)

 # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")