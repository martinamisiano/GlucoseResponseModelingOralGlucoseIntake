import numpy as np

def model(t, A, a, b):
    return A * (np.exp(-a*t) - np.exp(-b*t))
