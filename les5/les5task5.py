from random import randint

with open('task5.txt', 'w+') as f5:
    for i in range(21):
        f5.write(str(randint(0, 100)) + ' ')
    f5.seek(0)
    numbers = f5.readline().split()
    numbers = [int(num) for num in numbers]
    print(f'Набор чисел: {numbers} \nИх сумма равна {sum(numbers)}')
