import numpy as np
import matplotlib.pyplot as plt


def plotting(L, K, R, X):
    """
    Построение графиков построенной модели.
    
    Parameters:
    -------
    X : matrix
        Матрица построенных значений.
    L, K, R : array
        Массивы параметров модели.
    """
    for i in range(0, len(L)):
        plt.plot(np.arange(0, len(X[i])), X[i])
    plt.legend(gen_legend(L, K, R))
    plt.show()


def gen_legend(L, K, R):
    """
    Генерация легенды для графика.

    Parameters:
    -------
    L : array of int
        Массив размера окна модели.
    K, R : array of float
        Массивы параметров модели.

    Output:
    -------
    legend : array of string
        Массив с легендой графика.
    """
    legend = []
    for i in range(0, len(L)):
        legend.append(gen_signature(L[i], K[i], R[i]))
    return legend


def gen_signature(l, k, r):
    """
    Генерация подписей к графикам.

    Parameters:
    -------
    l, k, r : array
        Параметры модели.
    """
    signature = 'l={L}, k={K}, r={R}'.format(L=l, K=k, R=r)
    return signature
