#============================
def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i 
        temp = count
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

number = 40
ret = solution(number)
print("Solution: return value of the function is", ret, ".")