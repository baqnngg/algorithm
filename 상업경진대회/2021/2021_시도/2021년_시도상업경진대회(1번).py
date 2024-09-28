n = int(input())
for i in range(n):
    time = [24,0,0]
    todaytime,ftime = input().split()
    th,tm,ts = todaytime.split(":")
    fh,fm,fs = ftime.split(":")
    th,tm,ts = int(th),int(tm),int(ts)
    fh,fm,fs = int(fh),int(fm),int(fs)
    # 시간계산
    time[0] += fh-th
    # 분계산
    time[1] += fm
    if time[1] - tm < 0:
        time[0] -= 1
        time[1] += (60-tm)
    else: time[1] -= tm

    time[2] += fs
    if time[2] - ts < 0:
        if time[1] != 0:
            time[1] -= 1
        time[2] += (60-ts)
    else: time[2] -= ts

    print(time)