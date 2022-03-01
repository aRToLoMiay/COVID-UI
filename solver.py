import numpy as np

from input import *
from output import *


def multisolver(L, K, R, startX, n):
    """
    Последовательное построение модельных данных по списку параметров.

    Parameters:
    -------
    L, K, R : array
        Коэффициенты модели.
    startX : array
        Начальные данные модели.
    n : int
        Количество шагов.
    """
    X = []
    for i in range(0, len(L)):
        x = solver(L[i], K[i], R[i], startX[:L[i]], n)
        if x is not None:
            X.append(x)
    return X


def solver(l, k, r, startX, n):
    """
    Реализация схемы $ x_k - x_{k-1} = r (x_k - x_{k-l+1})(k - x_k) $.
    После преобразования схема обретает следующий вид:
    $$ rx_k^2 + (1 - rK - rx_{k-l+1}) + (rkx_{k-l+1} - x_{k-1}) = 0 $$
    В качестве решения $ x_k $ принимается больший из корней квадратного уравнения.
    В случае отрицательного дискриминанта для уравнения, алгоритм сообщает об ошибке и возвращает значение None.

    Parameters:
    -------
    l, k, r : array
        Параметры модели.
    startX : array
        Начальные модельные данные.
    n : int
        Количество шагов модели.
    """
    x = np.zeros((l + n), dtype=float)
    x[:len(startX)] = startX
    for i in range(l, n + l):
        a = r
        b = 1 - r * k - r * x[i - l + 1]
        c = r * k * x[i - l + 1] - x[i - 1]
        D = b ** 2 - 4 * a * c
        if D >= 0:
            x[i] = (-b + np.sqrt(D)) / (2 * a)
        else:
            print("ERROR! Discriminant lower than zero.")
            x = None
            break
    return x
