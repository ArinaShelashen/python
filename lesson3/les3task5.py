def sum_of_numbers():
    total = 0
    while True:
        user_data = input('Введите числа через пробел. Чтобы завершить суммирование, введите @: ').split()
        try:
            for i in range(len(user_data)):
                if user_data[i] == '@':
                    return print(f'Сумма чисел = {total}. Программа завершена.')
                total += int(user_data[i])
            print(f'Сумма чисел = {total}')
        except ValueError:
            return print('Неправильный тип данных. Попробуйте ещё раз.')


sum_of_numbers()
