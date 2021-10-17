from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]


def multiplier(a, b):
    return a * b


print(reduce(multiplier, my_list))
