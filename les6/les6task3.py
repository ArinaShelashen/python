class Worker:
    income_list = {"wage": 500, "bonus": 100}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    _income = income_list


class Position(Worker):

    def get_full_name(self):
        print(f'Worker name - {self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        salary = self._income['wage'] + self._income['bonus']
        print(f'Salary - {salary}$')


worker1 = Position('Tom', 'Brown', 'chemist')
# Проверка значений атрибутов:
# print(worker1.name)
# print(worker1.surname)
# print(worker1.position)
# print(worker1._income)
worker1.get_full_name()
worker1.get_total_income()
