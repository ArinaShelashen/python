class Car:

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = None

    def go(self):
        print(f'{self.color} {self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч \n Скорость превышена на {self.speed - 60} км/ч!')


class SportCar(Car):
    def __init__(self, speed, color, name, max_speed):
        Car.__init__(self, speed, color, name)
        self.max_speed = max_speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name} - {self.speed} км/ч\nСкорость превышена на {self.speed - 40} км/ч!')


class PoliceCar(Car):
    is_police = True


a = TownCar(90, 'Красный', 'Mercedes')
b = WorkCar(50, 'Черный', 'Reno')
c = SportCar(200, 'Красный', 'Ferrari', 400)
d = PoliceCar(70, 'Белый', 'Geely')
print(f'Машины:\n{a.color} {a.name}, полицейская - {a.is_police}'
      f'\n{b.color} {b.name}, полицейская - {b.is_police}'
      f'\n{c.color} {c.name}, полицейская - {c.is_police}'
      f'\n{d.color} {d.name}, полицейская - {d.is_police}')
a.go()
c.stop()
d.turn('направо')
b.show_speed()
