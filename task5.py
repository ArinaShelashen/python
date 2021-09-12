revenue = int(input('Выручка фирмы - '))
costs = int(input('Издержки фирмы - '))
profit = revenue - costs
if profit > 0:
    print('Фирма работает в прибыль.')
    print(f'Рентабельность выручки - {(revenue / profit):.2f}')
    staff = int(input('Число сотрудников в фирме - '))
    print(f'Прибыль в расчете на сотрудника - {(profit / staff):.2f}')
elif profit < 0:
    print('Фирма работает в убыток.')
else:
    print('Фирма работает в ноль.')
