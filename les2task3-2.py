calendar = {12: 'зима', 1: 'зима', 2: 'зима',
            3: 'весна', 4: 'весна', 5: 'весна',
            6: 'лето', 7: 'лето', 8: 'лето',
            9: 'осень', 10: 'осень', 11: 'осень',
            }
while True:
    month = input('Введите порядковый номер месяца: ')
    if month.isdigit() and int(month) in range(1, 13):
        print(f'Месяц №{month} - это {calendar.get(int(month))}')
        break
    else:
        print('Введите корректные данные')
