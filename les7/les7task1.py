class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix = ''
        for line in range(len(self.data)):
            for el in range(len(self.data[line])):
                matrix += str(self.data[line][el]) + ' '
            matrix += '\n'
        return str(matrix)

    def __add__(self, other):
        try:
            sum_matrix = []
            for line in range(len(self.data)):
                sum_matrix.append([])
                for el in range(len(self.data[line])):
                    sum_matrix[line].append(self.data[line][el] + other.data[line][el])
            return Matrix(sum_matrix)
        except IndexError:
            return 'Матрицы должны быть одинакового размера'


a = Matrix([[1, 2, 1], [2, 3, 1]])
b = Matrix([[4, 5, 2], [5, 6, 1]])
print(a)
print(b)
c = a+b
print(c)
