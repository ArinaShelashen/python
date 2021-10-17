class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def method_1(cls, date):
        try:
            day = int(date.split('-')[0])
            month = int(date.split('-')[1])
            year = int(date.split('-')[2])
            return day, month, year
        except ValueError:
            return 'Введите дату в правильном формате'
        except IndexError:
            return 'Введите дату в правильном формате'

    @staticmethod
    def method_2(date):
        try:
            if int(date.split('-')[0]) not in range(1, 32):
                return 'Число задано неверно'
            if int(date.split('-')[1]) not in range(1, 13):
                return 'Месяц задан неверно'
            if int(date.split('-')[2]) < 0:
                return 'Введите год нашей эры'
        except ValueError:
            return 'Введите дату в правильном формате'
        except IndexError:
            return 'Введите дату в правильном формате'
        else:
            return 'Дата задана верно'


print(Date.method_1('04-04-1982'))
print(Date.method_2('01-04-782'))
print(Date.method_1('04-ф-1982'))
print(Date.method_2('01-13-782'))
