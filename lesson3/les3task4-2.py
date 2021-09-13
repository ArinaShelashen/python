def my_func(x, y):
    if (type(x) == float or type(x) == int) and x > 0 and (type(y) == int and y < 0):
        exp = 1
        for i in range(abs(y)):
            exp /= x
        return exp
    else:
        return 'Тип данных задан неверно.'


print(my_func(10, -3))
