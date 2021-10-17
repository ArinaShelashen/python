storage = {}
office = {}


class Storage:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        storage[name] = quantity
        print(f'На склад поставлено {storage[name]} единиц объекта {self.name}')


class OfficeEquipment:
    def __init__(self, name, width, length, height):
        self.name = name
        self.width = width
        self.length = length
        self.height = height

    def move_to_storage(self):
        while True:
            try:
                storage_num = int(input(f'Сколько единиц техники {self.name} необходимо переместить на склад? '))
                storage_move = Storage(self.name, storage_num)
                break
            except ValueError:
                print('Введите целое число, без десятых')

    def move_to_office(self):
        try:
            office_num = int(input(f'Сколько единиц техники {self.name} необходимо поставить в офис? '))
            office[self.name] = office_num
            print(f'В офис доставлено {office_num} {self.name}')
        except ValueError:
            print('Введите целое число, без десятых')


class Printer(OfficeEquipment):
    def __init__(self, name, width, length, height, type_of_printing):
        OfficeEquipment.__init__(self, name, width, length, height)
        self.type_of_printing = type_of_printing


class Scanner(OfficeEquipment):
    def __init__(self, name, width, length, height, color):
        OfficeEquipment.__init__(self, name, width, length, height)
        self.color = color


class Copier(OfficeEquipment):
    def __init__(self, name, width, length, height, num_of_copies):
        OfficeEquipment.__init__(self, name, width, length, height)
        self.num_of_copies = num_of_copies


x = Copier('xerox', 612, 312, 312, 600)
x.move_to_storage()
x.move_to_office()
y = Printer('canon LBP', 423, 323, 212, 'laser')
y.move_to_storage()
y.move_to_office()
z = Scanner('Kyocera', 243, 199, 132, 'black/white')
z.move_to_storage()
z.move_to_office()
print(office)
print(storage)
