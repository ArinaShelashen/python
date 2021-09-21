num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('task4-1.txt', 'r') as f_1:
    for line in f_1:
        new_line = line.replace(line.split()[0], num_dict[line.split()[0]])
        with open('task4-2.txt', 'a', encoding='utf-8') as f_2:
            f_2.write(new_line)
