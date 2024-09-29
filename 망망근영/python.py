# def area_circle(r):
#     return r*r*3

# n = int(input())
# print(area_circle(n))


# select = int(input())
# n = int(input())

# def get_area_circle(n):
#     return n * n * 3

# def get_area_square(n):
#     return n * n

# if (select == 1):
#     print(get_area_circle(n))
# else:
#     print(get_area_square(n))



# def print_multi_table(n):
    
#     print(f"={n}단=")
#     for i in range(1, 10):
#         print(f"{n}*{i}={n*i}")

# def main():

#     num_tables = int(input())
    
#     for _ in range(num_tables):
#         table = int(input())
#         print_multi_table(table)



# i=0
# while i<5:
#     i=i+1
#     print("안녕하쌤")



# cnt=0
# while True:
#     cnt=cnt+1
#     print("안녕하쌤")
#     if cnt==5:
#         break;


# num = 0
# while True:
#     num = num + 1
#     print(num)
#     if num == 100:
#         break;


# n = int(input("정수 n을 입력하세요: "))

# i = 1

# while i <= n:
#     print(i)
#     i += 1



# n = int(input("정수 n을 입력하세요: "))

# i = 1

# while i <= n:
#     print(f"{i}*{i} = {i*i}")
#     i += 1



# n = int(input("정수 n을 입력하세요: "))

# s = 1
# e = 9

# print(f"=== {n}단 ===")

# while s <= e:
#     print(f"{n}*{s} = {n*s}")
#     s += 1



# data = list(map(int, input().split()))

# print(data)

# print(data[1])



n = int(input())
height = [int(input()) for _ in range(n)]
print(height[0] + height[1] + height[2] + height[3])