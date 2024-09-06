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



def print_multi_table(n):
    
    print(f"={n}단=")
    for i in range(1, 10):
        print(f"{n}*{i}={n*i}")

def main():

    num_tables = int(input())
    
    for _ in range(num_tables):
        table = int(input())
        print_multi_table(table)