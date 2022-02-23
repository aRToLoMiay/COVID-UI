# -*- coding: utf-8 -*-
import numpy as np

from input import *
from output import *
from solver import *

def start():
    """
    Base function.
    """
    tested = bool(int(input()))

    if tested:
        L, K, R, startX, n = get_params()
    else:
        L, K, R, startX, n = read_params()
    
    X = multisolver(L, K, R, startX, n)
    plotting(L, K, R, X)

start()
