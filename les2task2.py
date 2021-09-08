list_1 = input('Введите элементы списка через пробел: ').split(' ')
print(f'Исходный список: {list_1}')

for i in range(0, len(list_1) - 1, 2):
    temp = list_1[i]
    list_1[i] = list_1[i+1]
    list_1[i+1] = temp

print(f'Измененный список : {list_1}')
