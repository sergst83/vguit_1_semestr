# Вариант 9.
# 1. Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
# 2. В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.
import random

from functions import kranto, max_element, cut_matrix


def gen_matrix(n_, is_int=False):
    matrix = []
    for i in range(0, n_):
        layer = []
        matrix.append(layer)
        for j in range(0, n_):
            layer.append((random.uniform(-1000, 1000), random.randint(-1000, 1000))[is_int])

    return matrix


print("Задание 1")
matrix = gen_matrix(3, True)
k = int(input("Введите k: "))
print(f'Исходная матрица {matrix}')
result = kranto(k, matrix)
print(f"Число элементов кратных k: {result[0]}")
print(f"Максимальный из элементов кратных k: {result[1]}")

print('________________')

print("Задание 2")
n = int(input("Задайте размерность квадратной матрицы n: "))

matrix = gen_matrix(n)
print(f"Сгенерирована матрица n x n: {matrix}")

max_el = max_element(matrix)
print(f'Максимальный элемент {max_el[0]} i: {max_el[1]}, j: {max_el[2]}')

print(f"Матрица порядка n-1: {cut_matrix(matrix, max_el[1], max_el[2])}")
