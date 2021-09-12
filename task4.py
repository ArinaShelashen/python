num = int(input('Введите целое положительное число: '))
max_num = 0
while num != 0:
    last_num = num % 10
    num = num // 10
    if last_num > max_num:
        max_num = last_num
print(f'Самая большая цифра в числе - {max_num}')
