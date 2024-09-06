def solution(record):
    answer = []
    cc = {}
    kk = []
    for c in record:
        d = list(c.split(" "))
        if d[0] == "Enter":
            cc[d[1]] = d[2]
            kk.append([d[1],"님이 들어왔습니다."])
        elif d[0] == "Leave":
            kk.append([d[1],"님이 나갔습니다."])
        elif d[0] == "Change":
            cc[d[1]] = d[2]
    for c in kk:
        answer.append(f'{cc[c[0]]}{c[1]}')
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))