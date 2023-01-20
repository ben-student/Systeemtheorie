import numpy as np
import matplotlib.pyplot as plt


def db(x):
    x = 20*np.log10(np.abs(x))
    return x
