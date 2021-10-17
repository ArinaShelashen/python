with open("task2.txt") as f:
    lines_num = 0
    for line in f:
        lines_num += 1
        words_num = len(line.split())
        print(f"В строке номер {lines_num} - {words_num} слов(а)")
print(f'Всего строк - {lines_num}')
