# 해시 쓰는법 =============
#1 어떻게 선언하는지
f_dict = {'apple':1,'banana':2,'orange':3}
print(f_dict)

#2 : 찾는법
a = input()
if a in f_dict:
    print(f"{a}: {f_dict[a]}")
else:
    print(f"{a}는 딕셔너리에 존재하지 않는다.")

#3 : 바꾸는법
b,c = input().split()
f_dict[b] = c
print(f_dict)

#4 : 삭제하는법
a = input()
del f_dict[a]
print(f_dict)