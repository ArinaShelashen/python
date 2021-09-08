user_string = input('Введите несколько слов. Отделяйте их друг от друга пробелами - ').split(' ')
for ind, el in enumerate(user_string):
    print(ind + 1, el[:10])
