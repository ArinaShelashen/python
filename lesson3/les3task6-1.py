def int_func(word):
    return word.capitalize()


print(int_func('text'))

# Task6 Part2

user_string = input('Введите слова, разделенные пробелом: ').split()
for i in range(len(user_string)):
    user_string[i] = int_func(user_string[i])
result = ' '.join(user_string)
print(result)
