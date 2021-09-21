with open("user_file.txt", "w") as u_file:
    while True:
        new_line = input('Введите новую строку. Чтобы завершить, нажмите Enter: ')
        if new_line == '':
            break
        else:
            u_file.write(new_line + '\n')
