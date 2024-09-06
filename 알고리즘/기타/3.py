import sys
input = sys.stdin.readline

vc,vt,t,k,d = map(int,input().split())
pos = t*vc
rc = 0

while (d-pos)/vc > d/vt:
    pos += (pos/(vt-vc)) * vc
    rc += 1
    pos += (pos/vt) * vc
    pos += k * vc

print(rc)