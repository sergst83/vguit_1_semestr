def kranto(k_, matrix_):
    l = len(matrix_)
    count = 0
    kranto_k = []
    for i in range(0, l):
        for j in range(0, l):
            element = matrix_[i][j]
            if element % k_ == 0:  # кратно k
                count += 1
                kranto_k.append(element)

    return count, max(kranto_k)


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
            if j == j_:
                continue
            layer.append(matrix_[i][j])
        new_matrix.append(layer)

    return new_matrix
