def solution(price, grade):
    answer = 0
    if grade == "S": answer = price*0.95
    elif grade == "G": answer = price*0.9
    elif grade == "V": answer = price*0.85
    return int(answer)

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print("Solution: return value of the function is", ret1, ".")
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)
print("Solution: return value of the function is", ret2, ".")