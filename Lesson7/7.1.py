"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_one)):

            for j in range(len(self.list_two[i])):
                matrix[i][j] = self.list_one[i][j] + self.list_two[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self, matrix=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[7, 10, 7],
                    [2, 5, 23]],
                   [[2, 7, 6],
                    [15, 7, 42]])

print(my_matrix.__add__())
