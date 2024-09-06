h,m,s = map(int,input().split())
cnt = 0
for i in range(h*3600+m*60+s+1):
    h = i // 3600
    m = (i-h*3600)//60
    s = i%60
    if str(h).count("1") or str(m).count("1") or str(s).count("1"):
        cnt += 1
print(cnt)