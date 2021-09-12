# rating = [7, 5, 3, 3, 1]
# while True:
#     act = input('Для ввода нового элемента рейтинга введите 1, для выхода введите 2 - ')
#     if act == '1':
#         print(f'Текущий рейтинг: {rating}')
#         new_el = int(input('Введите новый элемент рейтинга: '))
#         rating.append(new_el)
#         print(sorted(rating, reverse=True))
#     elif act == '2':
#         break
#     else:
#         print('Введите корректное значение')

my_list = [9, 8, 7, 6, 6, 3, 3, 2]
new = int(input('enter'))
i = 0
for n in my_list:
    if new <= n:
        i +=1
    elif new > n:
        break
my_list.insert(i, float(new))
print(my_list)