
def load_data(file_name: str = 'sample') -> list:
    file = open(file_name)
    try:
        date = file.readlines()
    finally:
        file.close()
    matrix = []
    for line in date[1:]:
        matrix.append(line.strip().split()[:])
    return matrix


def cut_name(matrix: list) -> list:
    new_matrix = []
    for line in matrix:
        new_matrix.append(line[1:])
    return new_matrix


def loss_table(matrix: list) -> list:
    print(matrix)
    result = []

    for x in range(0, len(matrix)):
        maks_list = []
        help = []
        for y in range(0, len(matrix[x])):
            maks_list.append(matrix[x][y])
        for y in range(0, len(matrix[x])):
            help.append(float(max(maks_list)) - float(matrix[x][y]))
        result.append(help)
    return result


def mini_maks(matrix: list) -> float:
    matrix = cut_name(matrix)
    min_list = []
    for mini in matrix:
        min_list.append(min(mini))

    return max(min_list)


def maks_maks(matrix: list) -> float:
    matrix = cut_name(matrix)
    maks_list = []
    for maks in matrix:
        maks_list.append(max(maks))

    return max(maks_list)


def k_hurwicz(matrix: list, factor: float = 0.5) -> tuple:
    matrix = cut_name(matrix)
    result = []
    factor = float(factor)
    for line in matrix:
        result.append(factor * float(min(line)) + (1 - factor) * float(max(line)))
    return result, max(result)


def k_bayesa(matrix: list, *args) -> tuple:
    matrix = cut_name(matrix)
    probability = []
    result = []

    for x in args:
        probability.append(x)
    for line in matrix:
        v = 0
        for x in range(len(line)):
            v += float(probability[x]) * float(line[x])
        result.append(v)

    return result, max(result)


def k_savage(matrix: list) -> tuple:
    matrix = cut_name(matrix)
    matrix = loss_table(matrix)
    result = []
    for line in matrix:
        result.append(max(line))

    return result, max(result)


def find_in_matrix(matrix: list, value: float) -> list:
    result = []
    for line in matrix:
        for i in range(len(line)):
            if float(line[i]) == float(value):
                result.append(line[0])
    return result


def find_in_result(result: tuple) -> float:
    return result[0].index(result[1])



#m = load_data()
#print(find_in_matrix(m, mini_maks(m)))
##print(find_in_matrix(m, maks_maks(m)))
#print(find_in_result(k_hurwicz(m)))
#print(find_in_result(k_bayesa(m, 1/2, 1/2, 1/2, 1/2)))
#print(k_savage(m))