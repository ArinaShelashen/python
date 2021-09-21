lines_num = 0
ave_income = 0
print('Менее 20000 зарабатывают:')
with open("task3.txt", 'r', encoding='utf-8') as f:
    try:
        for line in f:
            lines_num +=1
            ave_income += float(line.split()[1])
            if float(line.split()[1]) < 20000:
                print(line.split()[0])
        ave_income /= lines_num
        print(f'Средний доход - %.2f' % ave_income)
    except ValueError:
        print('Ошибка в типе данных дохода')
