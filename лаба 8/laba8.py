# Вариант 9.
# 1. Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
# 2. В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.
import random

print("Задание 1")
def kranto(k_, matrix_):
    l = len(matrix_)
    count = 0
    kranto_k = []
    for i in range(0, l):
        for j in range(0, l):
            element = matrix_[i][j]
            if element % k_ == 0: # кратно k
                count += 1
                kranto_k.append(element)

    return count, max(kranto_k)


matrix = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]
k = int(input("Введите k: "))
print(f'Исходная матрица {matrix}')
result = kranto(k, matrix)
print(f"Число элементов кратных k: {result[0]}")
print(f"Максимальный из элементов кратных k: {result[1]}")

print('________________')

print("Задание 2")
def gen_matrix(n_):
    matrix = []
    for i in range(0, n_):
        layer = []
        matrix.append(layer)
        for j in range(0, n_):
            layer.append(random.randint(-1000, 1000))

    return matrix


def max_element(matrix_: [[]]):
    max_value = 0
    i_ = 0
    j_ = 0
    val_ = 0
    for i in range(0, len(matrix_)):
        for j in range(0, len(matrix_)):
            if max_value < abs(matrix_[i][j]):
                max_value = abs(matrix_[i][j])
                i_ = i
                j_ = j
                val_ = matrix_[i][j]

    return val_, i_, j_


def cut_matrix(matrix_: [[]], i_: int, j_: int):
    new_matrix = []
    for i in range(0, len(matrix_)):
        if i == i_:
            continue
        layer = []
        for j in range(0, len(matrix_)):
            if j == j_ or i == i_:
                continue
            layer.append(matrix_[i][j])
        new_matrix.append(layer)

    return new_matrix


n = int(input("Задайте размерность квадратной матрицы n: "))
matrix = gen_matrix(n)
print(f"Сгенерирована матрица n x n: {matrix}")

max_el = max_element(matrix)
print(f'Максимальный элемент {max_el[0]} i: {max_el[1]}, j: {max_el[2]}')

print(f"Матрица порядка n-1: {cut_matrix(matrix, max_el[1], max_el[2])}")