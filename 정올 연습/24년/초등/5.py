# 마법의 보물상자를 열어라

# 입력 문자열을 공백 기준으로 나누어 리스트로 저장
# 예: "hope light + brave - $" → ['hope', 'light', '+', 'brave', '-', '$']
tokens = input().split()

# 연산을 처리할 스택 (데이터를 잠시 저장하는 자료구조)
stack = []

# 토큰(단어 또는 연산자)을 하나씩 꺼내면서 처리
for token in tokens:
    if token == "$":
        # '$' 기호를 만나면 입력 종료
        break

    if token == "+":
        # '+' 연산: 두 문자열을 이어 붙임
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)

    elif token == "-":
        # '-' 연산: 두 문자열 중 짧은 것 선택
        # 길이가 같으면 먼저 들어온 a를 선택
        b, a = stack.pop(), stack.pop()
        stack.append(a if len(a) <= len(b) else b)

    elif token == "*":
        # '*' 연산: 각각의 문자열을 2번 반복해서 합침
        b, a = stack.pop(), stack.pop()
        stack.append(a * 2 + b * 2)

    elif token == "/":
        # '/' 연산: 각 문자열의 앞 절반만 잘라서 이어붙임
        b, a = stack.pop(), stack.pop()
        stack.append(a[:len(a)//2] + b[:len(b)//2])

    else:
        # 일반 단어일 경우 스택에 그대로 저장
        stack.append(token)

# 모든 연산이 끝난 후, 스택에 정확히 하나의 결과만 남아야 정상
if len(stack) == 1:
    print(stack[0])  # 최종 암호 출력
else:
    print("ERROR")  # 스택에 값이 여러 개 남았거나 비었을 경우 오류
