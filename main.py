# -*- coding: utf-8 -*-
from solver import *


tested = False
if tested:
# Получение тестовых параметров модели.
    L, K, R, startX, n = get_params()
else:
# Ввод параметров модели.
    L, K, R, startX, n = read_params()

# Построение модельных данных.
X = multisolver(L, K, R, startX, n)

# Построение графиков.
plotting(L, K, R, X)
