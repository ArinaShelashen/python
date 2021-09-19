from itertools import cycle

my_list = ['Q', 'W', 'E', 'R', 'T', 'Y']
c = 0
for el in cycle(my_list):
    if c == 20:
        break
    else:
        print(el)
        c +=1
