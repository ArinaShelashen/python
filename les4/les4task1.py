from sys import argv

script_name, work_hours, hourly_rate, extra = argv
print('Зарплата составит ', work_hours*hourly_rate+extra)
