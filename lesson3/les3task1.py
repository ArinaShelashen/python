def division():
    try:
        divisible = float(input('Введите делимое: '))
        divisor = float(input('Введите делитель: '))
        result = round(divisible / divisor, 2)
    except ZeroDivisionError:
        return print('На ноль делить нельзя.')
    return print(f'Результат деления - {result}')


division()
