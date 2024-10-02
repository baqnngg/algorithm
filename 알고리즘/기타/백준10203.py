n = int(input())
for _ in range(n):
    a = input()
    ss = 0
    for i in list(a):
        if i == 'a': ss += 1
        elif i == 'e': ss += 1
        elif i == 'i': ss += 1
        elif i == 'o': ss += 1
        elif i == 'u': ss += 1
    print(f"The number of vowels in {a} is {ss}.")