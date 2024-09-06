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
            elif c == ")" or c == "}" or c == "]":
                if stack:
                    for i in stack:
                        if (c == ")" and i == "(") or (c == "]" and i == "[") or (c == "}" and i == "{"):
                            if not stack:
                                answer -= 1
                                break
                            else:
                                stack.pop()
                elif not stack:
                    answer -= 1
                    break
        if stack:
            stack = []
            continue
        else:
            answer += 1

    return answer

print(solution(input()))