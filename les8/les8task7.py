class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0:
            return f'{self.b}i'
        else:
            if self.b > 0:
                return f'{self.a} + {self.b}i'
            elif self.b == 0:
                return f'{self.a}'
            else:
                return f'{self.a} - {-self.b}i'

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


x = ComplexNum(2, -3)
y = ComplexNum(3, 2)
z = x + y
q = x * y
print(x)
print(y)
print(z)
print(q)
