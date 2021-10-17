report = {}
with open('task6.txt', 'r', encoding='utf-8') as f6:
    for line in f6:
        hours = [int(i) for i in line.split() if i.isnumeric()]
        report[line.split()[0][:-1]] = sum(hours)
    print(report)
