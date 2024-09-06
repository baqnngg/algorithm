import sys
input = sys.stdin.readline
# [1] 입력 받기
n, m = map(int, input().split())
time_icebreak = [0] * (n + 2)
ice = [0] * (n+2)
st = []
answer = 0

for i in range(1, n+1):
    ice[i] = int(input())


# [2] 고드름 부러지는 시간 계산하기
for i in range(1, n + 1):
    # 자랄 수 있는 고드름 후보 스택에 저장하기
    # 파이썬에서는 리스트가 스택 역할, append/pop
    if ice[i] > ice[i - 1] and ice[i] > ice[i + 1]:
        st.append(i)

while st:
    a = st.pop()
    time_icebreak[a] += (m - ice[a]) # 고드름 후보가 부러질 때까지 걸리는 시간 계산
    ice[a] = 0 # 고드름 부러뜨리기
    
    # 인접한 고드름에 경과시간 업데이트하기
    time_icebreak[a - 1] = max(time_icebreak[a - 1], time_icebreak[a]) 
    time_icebreak[a + 1] = max(time_icebreak[a + 1], time_icebreak[a])
    
    # 자랄 수 있는 고드름 후보 스택에 저장하기
    if ice[a - 1] > 0 and ice[a - 1] > ice[a - 2]:
        st.append(a - 1)
    if ice[a + 1] > 0 and ice[a + 1] > ice[a + 2]:
        st.append(a + 1)
    
    answer = max(answer, time_icebreak[a]) # 정답 업데이트하기
    
# [3] 정답 출력
print(answer)