def solution(shirt_size):
    answer = []
    a = ['XS', 'S', 'M', 'L', 'XL', "XXL"]
    for i in range(len(a)):
        answer.append(shirt_size.count(a[i]))
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("Solution: return value of the function is ", ret, " .")