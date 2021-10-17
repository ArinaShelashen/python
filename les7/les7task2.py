from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param
        self.fabric_quant = 0

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):

    @property
    def fabric(self):
        self.fabric_quant = self.param / 6.5 + 0.5
        return f'Расход ткани для пальто - {round(self.fabric_quant, 2)}'


class Costume(Clothes):

    @property
    def fabric(self):
        self.fabric_quant = self.param * 2 + 0.3
        return f'Расход ткани для костюма - {round(self.fabric_quant, 2)}'


a = Coat(5)
b = Costume(2)
print(a.fabric)
print(b.fabric)
