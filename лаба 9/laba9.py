# Задание
# Для заданий из практической работы №8 для своего варианта.
# Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
# И вывод результатов в файл (имя: ФИО_группа_vivod.txt)
from functions import kranto, max_element, cut_matrix


def to_number(str_):
    if str(str_).find('.') > 0:
        return float(str_)
    else:
        return int(str_)


def read_matrix(file_name: str):
    matrix = []
    with open(file_name) as file:
        for line in file.readlines():
            layer = list(
                map(
                    lambda l: to_number(l),
                    line.split(" ")
                )
            )
            matrix.append(layer)
        file.close()

    return matrix


def write_result(file_name: str, res: str):
    with open(file_name, 'w') as file:
        file.write(res)
        file.close()


print("Задание 1")
file_in = "ССВ_ЗИТ-22м_vvod_1.txt"
file_out = "ССВ_ЗИТ-22м_vivod_1.txt"
matrix = read_matrix(file_in)

k = int(input("Введите k: "))
print(f'Исходная матрица из файла {file_in}: {matrix}')
result = kranto(k, matrix)
result = f'''\
Число элементов кратных k: {result[0]}
Максимальный из элементов кратных k: {result[1]}\
'''
print(result)
write_result(file_out, result)
print(f'Результат сохранен в файл {file_out}')

print('________________')

print("Задание 2")
file_in = "ССВ_ЗИТ-22м_vvod_2.txt"
file_out = "ССВ_ЗИТ-22м_vivod_2.txt"

matrix = read_matrix(file_in, )
print(f"Считана матрица {len(matrix)} x {len(matrix)} из файла {file_in}: {matrix}")

max_el = max_element(matrix)
result = f'''\
Максимальный элемент {max_el[0]} i: {max_el[1]}, j: {max_el[2]}
Матрица порядка n-1: {cut_matrix(matrix, max_el[1], max_el[2])}\
'''
print(result)
write_result(file_out, result)
print(f'Результат сохранен в файл {file_out}')
