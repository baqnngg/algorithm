s=input()
bomb=list(input())
n=len(bomb) #터지는 문자열의 길이
stack=[]
for c in s:
    stack.append(c)
    if stack[-n:]==bomb:  #??????????
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')