#===============
def solution(characters):
 result = ""
 result += characters[0]
 for i in range(len(characters)):
    if characters[i - 1] != characters[i]:
        result += characters[i]
 return result

characters = "senteeeencccccceeee"
ret = solution(characters)
#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")