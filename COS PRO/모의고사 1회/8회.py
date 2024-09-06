#===========================
def solution(sentence):
 str = '' 
 for c in sentence:
    if c != '.' or c != ' ':
        str += c
        size = len(str)
 for i in range(size // 2):
    if str[i] != str[size - 1 - i]:
        return False
 return True

sentence1 = "never odd or even."
ret1 = solution(sentence1)

print("Solution: return value of the function is", ret1, ".")
sentence2 = "palindrome"
ret2 = solution(sentence2)
print("Solution: return value of the function is", ret2, ".")