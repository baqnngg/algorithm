a,b = map(int,input().split())
c,d = map(int,input().split())

# [설계2] 최대공약수 구하기 함수 설계(유클리드 호제법)
def gcd(x, y):
    if x<y: # (1) 크기 정렬
        x, y = y, x
    while y!= 0: # (2) y가 0이 될때까지 서로 제거하기(유클리드 호제법)
        r = x%y
        x = y
        y = r
    return x # (3) y가 0일 때의 x값이 최대공약수

#최대공약수 받아서 오기
f = gcd((b*c + a*d), b*d)
#최대공약수로 나눈 나머지 값 구하기 (기약분수)
print((b*c + a*d)//f,(b*d)//f)