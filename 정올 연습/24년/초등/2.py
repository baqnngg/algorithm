# '만 나이' 계산하기
birth_y, birth_m, birth_d = list(map(int, input().split("/")))
age_y, age_m, age_d = list(map(int, input().split("/")))

age_years = age_y - birth_y

if (age_m, age_d) < (birth_m, birth_d):
    age_years -= 1

if age_years == 0:
    age_months = age_m - birth_m
    if age_months <= 0:
        age_months += 12
    if age_d < birth_d:
        age_months -= 1
    if birth_y == age_y and age_months == 12:
        age_months = 0
    print(f"{age_months}M")
else:
    print(f"{age_years}Y")