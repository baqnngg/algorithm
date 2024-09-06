# 1. 같이하기 : 보석과 돌
def s(J,S):
    f = {}
    cnt = 0
    for c in S:
        if c not in f: f[c] = 1
        else: f[c] += 1
    for c in J:
        if c in f:
            cnt += f[c]
    return cnt

J = "aA"
S = "aAAbbbb"
print(s(J,S))

# 2. 따라하기 : 완주하지 못한 선수
def solution(participant, completion):
    f = {}
    answer = 0
    for c in participant:
        if c not in f: 
            f[c] = 1
        else: 
            f[c] += 1
    for c in completion:
        if c in f:
            f[c] -= 1

    for i in f:
        if f[i] != 0:
            answer = i

    return answer

P = ["mislav", "stanko", "mislav", "ana"]
C = ["stanko", "ana", "mislav"]
print(solution(P,C))