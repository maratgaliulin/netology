# Метрики расстояний

import numpy as np


# a = np.array([[4,2,1], [1,3,0], [0,5,4]])
# b = np.array([4,12,-3])
# c = np.linalg.solve(a,b)
#
# print(c)


def inverse_nparr_creator():
    int_input = int(input("Введите количество элементов в массиве: "))
    inverse_arr = np.arange(0, int_input)[::-1]  # можно сделать np.arange(int_input-1, -1, -1), но получается менее
    # красиво
    print(f'Массив: {inverse_arr}')


def inverse_matrix_creator():
    int_input = int(input("Введите количество элементов в матрице: "))
    inverse_matrix = np.diag(np.arange(int_input, 0, -1))
    print(np.arange(int_input, 0, -1))
    print(f'Матрица: {inverse_matrix}')
    print(f'Сумма элементов матрицы: {sum(sum(inverse_matrix))}')


def client_compare(next_user_stats_input: np.ndarray):
    users_stats = np.array(
        [
            [2, 1, 0, 0, 0, 0],
            [1, 1, 2, 1, 0, 0],
            [2, 0, 1, 0, 0, 0],
            [1, 1, 2, 1, 0, 1],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 5],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 3],
            [1, 0, 0, 2, 1, 4]
            ]
        )

    def cosine(a, b):
        aLength = np.sqrt((a * a).sum())
        bLength = np.sqrt((b * b).sum())
        return np.dot(a, b) / (aLength * bLength)

    cosine_arr = np.array([cosine(x, next_user_stats_input) for x in users_stats])
    print(f'Массив из косинусов между векторами нового и предыдущих клиентов: {cosine_arr}')
    print(f'Индекс самого похожего клиента из клиентской базы: {cosine_arr.argmax()}')

# inverse_nparr_creator()

# inverse_matrix_creator()

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

client_compare(next_user_stats)
