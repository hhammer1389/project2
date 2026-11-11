import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
def linear(m, x, b):
    return m*x+b
def slope_units(x_units, y_units):
    y_units = y_units.rstrip("s")
    x_units = x_units.rstrip('s')
    return y_units + "/" + x_units
def print_equation(m, b, y_units, x_units):
    m = str(m) +(slope_units(x_units, y_units))
    b = str(b) +(y_units)
    print("The equation of the line is y=", m, "x+", b)
