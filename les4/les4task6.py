from itertools import count

start_num = int(input('Введите число меньшее 26 - '))

for num in count(start_num):
    if num > 26:
        break
    else:
        print(num)
