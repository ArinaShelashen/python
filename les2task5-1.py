rating = [7, 5, 3, 3, 1]
while True:
    act = input('Для ввода нового элемента рейтинга введите 1, для выхода введите 2 - ')
    if act == '1':
        print(f'Текущий рейтинг: {rating}')
        new_el = int(input('Введите новый элемент рейтинга: '))
        for i in range(len(rating)):
            if new_el > rating[i]:
                rating.insert(i, new_el)
                break
        print(f'Новый рейтинг: {rating}')
    elif act == '2':
        break
    else:
        print('Введите корректное значение')
