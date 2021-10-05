class Cell:

    def __init__(self, slots):
        self.slots = slots

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __sub__(self, other):
        if self.slots >= other.slots:
            return Cell(self.slots - other.slots)
        else:
            return Cell('Нельзя из меньшей клетки вычесть большую.')

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __truediv__(self, other):
        return Cell(round(self.slots / other.slots))

    def make_order(self, row_slots):
        output = ''
        for i in range(self.slots // row_slots):
            output += '*' * row_slots + '\n'
        output += '*' * (self.slots % row_slots)
        return output


a = Cell(12)
b = Cell(3)
c = a + b
d = b - a
e = a - b
f = a * b
g = a / b
print(c.slots)
print(d.slots)
print(e.slots)
print(f.slots)
print(g.slots)
print(a.make_order(5))
