"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических
операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()). Данные
методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
"""


class Cell:
    def __init__(self, quantity):
        self.quantity: int = quantity

    def __str__(self):
        return f'{self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print(
            'Отрицательное значние')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cell_1 = Cell(10)
cell_2 = Cell(5)
print("\n")
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2.make_order(5))
print(cell_1.make_order(10))
print(cell_1 / cell_2)
