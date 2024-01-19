# count = 0
# while count <= 30:
#     if count % 3 == 0:
#         print('Hoorah')
#         count += 1
#     else:
#         print(count)
#         count += 1

# for i in range(30):
#     if i % 3 == 0:
#         print('Bibsy')
#     else:
#         print(i)

# my_set = {1, 2, 3, 5, 5, 5}
# print(6 in my_set)

# def count(a=2, b=2):
#     print(a+b)

# count(1)

# def get_i (max_int: int) -> list:
#     return [i for i in range(1, max_int, 2)]
# print(get_i(8))

# def func(letters: list) -> str:
#     return ' '.join(letters)
# print(func(['R', 2, '-', 'D', 2]))

def fuzz(a):
    if a % 5 == 0:
        return 5
    elif a % 3 == 0:
        return 3
    elif a % 15 == 0:
        return 15
print(fuzz(15))