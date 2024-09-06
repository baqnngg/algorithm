from collections import deque
def solution(s):
    answer = 0
    a = deque(list(s))
    stack = []
    b = a.pop()
    a.insert(0,b)
    for _ in range(len(a)):
        b = a.popleft()
        a.append(b)
        for c in a:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif (c == ")" and stack.count("(") != 0) or (c == "]" and stack.count("[") != 0) or (c == "}" and stack.count("{") != 0):
                if not stack:
                    answer -= 1
                    break
                else:
                    stack.pop()
        if stack:
            break
        else:
            answer += 1

    return answer