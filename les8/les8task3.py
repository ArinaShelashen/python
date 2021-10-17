class NotNumError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    a = input('Введите следующий элемент списка. Чтобы остановить программу, введите @: ')
    try:
        if a == '@':
            print('Программа завершена.')
            break
        elif not a.isdigit():
            raise NotNumError('В списке должны быть только числа.')
        else:
            user_list.append(a)
    except NotNumError as err:
        print(err)
    else:
        print('Элемент включен в список.')
