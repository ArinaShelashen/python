def my_func(arg1, arg2, arg3):
    sum_max = arg1 + arg2 + arg3 - min(arg1, arg2, arg3)
    return sum_max


result = my_func(26, 0, -20)
print(result)
