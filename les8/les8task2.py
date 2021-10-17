class ZeroDivEr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')

try:
    c = int(b)
    if c == 0:
        raise ZeroDivEr('На ноль делить нельзя')
    d = int(a) / c
except ValueError:
    print('Вы ввели не число')
except ZeroDivEr as err:
    print(err)
else:
    print('Частное - ', d)
