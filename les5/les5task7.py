import json

profit_dict = {}
loss_dict = {}
ave_profit = 0
count = 0
with open('task7.txt', 'r') as f7:
    for line in f7:
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit >= 0:
            count += 1
            ave_profit += profit
            profit_dict[line.split()[0]] = profit
        else:
            loss_dict[line.split()[0]] = profit
average = {'average_profit': int(ave_profit / count)}
final_list = [profit_dict, loss_dict, average]
print(final_list)


with open('task7.json', 'w') as json_file:
    json.dump(final_list, json_file)
