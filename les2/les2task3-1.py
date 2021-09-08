season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
while True:
    month = input('Введите порядковый номер месяца: ')
    if month.isdigit() and int(month) in range(1, 13):
        print(f'Месяц №{month} - это {season[int(month) - 1]}')
        break
    else:
        print('Введите корректные данные')
