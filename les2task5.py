rating = [7, 5, 3, 3, 1]
while True:
    act = input('Для ввода нового элемента рейтинга введите 1, для выхода введите 2 - ')
    if act == '1':
        print(f'Текущий рейтинг: {rating}')
        new_el = int(input('Введите новый элемент рейтинга: '))
        rating.append(new_el)
        print(sorted(rating, reverse=True))
    elif act == '2':
        break
    else:
        print('Введите корректное значение')
