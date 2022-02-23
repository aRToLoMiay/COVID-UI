import numpy as np


def get_params():
    """
    Получение тестовых значений параметров алгоритма.

    Output:
    -------
    L, K, R : array
        Массивы параметров модели.
    startX : array
        Начальные данные модели.
    n : int
        Количество шагов.
    """
    L = np.array([3.0, 4.0, 5.0], dtype=int)
    K = np.array([0.2, 0.25, 0.35])
    R = np.array([1.5, 1.25, 1.0])

    startX = (np.arange(0, np.max(L)) + 1)**2
    
    n = 1000

    return L, K, R, startX, n


def read_params():
    """
    Чтение параметров алгоритма из консоли.

    Output:
    -------
    L, K, R : array
        Массивы параметров модели.
    startX : array
        Начальные данные модели.
    n : int
        Количество шагов. 
    """
    print("Input parameters lists.")
    print("\tInput l:")
    L = convert_str(input())
    L = np.array(L, dtype=int)
    print("\tInput k:")
    K = convert_str(input())
    print("\tINput r:")
    R = convert_str(input())
    L, K, R = params_check(L, K, R)

    print("Input started data ({num} values):".format(num=np.max(L)))
    startX = convert_str(input())

    print("Input number of steps:")
    n = int(input())

    return L, K, R,startX, n


def convert_str(str, delim=';'):
    """
    Конвертация строки параметров в массив float.

    Parameters:
    -------
    str : string
        Строка с параметрами.
    delim : string
        Разделитель.

    Output:
    -------
    res : array of float
        Массив разделённых значений.
    """
    ar = np.array(str.split(delim))
    n = len(ar)
    res = np.zeros_like(ar, dtype=float)
    for i in range(n):
        res[i] = float(ar[i])
    return res


def params_check(L, K, R):
    """
    Обрезка списка параметров в случае ошибки ввода.

    Parameters:
    -------
    L, K, R : array
        Массивы параметров модели.

    Output:
    -------
    L, K, R : array
        Обрезанные с конца массивы параметров.
    """
    n = min(len(L), len(K), len(R))
    if ((n != len(L)) or (n != len(K)) or (n != len(R))):
        print("WARNING! Different number of parameters. Parameters lists will cuttet for single size.")
    L = L[:n]
    K = K[:n]
    R = R[:n]
    return L, K, R
