# Вариант 9.
# 1. Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму
# его цифр и т. д. Через сколько таких действий получится нуль?
# 2. Даны 3 различных массива целых чисел. В каждом массиве найти
# произведение элементов и среднеарифметическое значение.
from functools import reduce

print("Задание 1")
def sum_digits(x):
    return sum(list(map(lambda n: int(n), list(str(x)))))

number = input('Введите число: ')
s = int(number) - sum_digits(number)
print(f's - sum_digits(s) = {s}')
iter_count = 1
while s > 0:
    s = s - sum_digits(s)
    print(f's - sum_digits(s) = {s}')
    iter_count += 1

print(f'Для числа {number} 0 получится через {iter_count} действий')

print('________________')

print("Задание 2")
def proisv(array):
    return reduce(lambda a, b : a * b, array)

def sr_arif(array):
    return sum(array) / len(array)

arr_1 = [i for i in range(0, 10)]
arr_2 = [i for i in range(100, 110)]
arr_3 = [i for i in range(1100, 1110)]

print("Массив 1: " + str(arr_1))
print("Массив 2: " + str(arr_2))
print("Массив 3: " + str(arr_3))

print("Произведение элементов массива 1: " + str(proisv(arr_1)))
print("Произведение элементов массива 2: " + str(proisv(arr_2)))
print("Произведение элементов массива 3: " + str(proisv(arr_3)))

print("Среднее арифметическое элементов массива 1: " + str(sr_arif(arr_1)))
print("Среднее арифметическое элементов массива 2: " + str(sr_arif(arr_2)))
print("Среднее арифметическое элементов массива 3: " + str(sr_arif(arr_3)))

