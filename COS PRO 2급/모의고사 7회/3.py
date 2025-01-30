def func_a(arr):
    ret = [0, 0]
    for x in arr:
        if x >= 0:
            ret[0]+= x
        else:       
            ret[1]+= x
    return ret

def func_b(arr):
    ret = arr[0] - arr[1]
    if ret < 0:
        return abs(ret)
    else:
        return abs(ret)

    
def func_c(arr):
    ret = []
    for a in arr:
        ret.append(sum(a))
    return ret       
    
def solution(arr2d):
    arr = func_c(arr2d)
    vnum = func_a(arr)
    num = func_b(vnum)
    return num

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr2d = [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5], [3, 3, 3, -3, -3], [5, 5, -5, -5, -5]]
ret = solution(arr2d)
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")