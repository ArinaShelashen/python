class Stationary:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    title = 'Ручка'

    def draw(self):
        return f'Вы рисуете прибором под названием {self.title}'


class Pencil(Stationary):
    title = 'Карандаш'

    def draw(self):
        return f'Вот-вот будет создан шедевр! А это всего лишь - {self.title}'


class Handle(Stationary):
    title = 'Маркер'

    def draw(self):
        return f'В вашей руке сейчас - {self.title}'


a = Pen()
b = Pencil()
c = Handle()
print(a.draw())
print(b.draw())
print(c.draw())
