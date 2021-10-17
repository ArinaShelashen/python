def fact(finish_number):
    factorial = 1
    for el in range(1, finish_number+1):
        factorial *= el
        yield el, factorial


n = int(input('Введите последнее число: '))
for num, result in fact(n):
    print(f'{num}! = {result}')
