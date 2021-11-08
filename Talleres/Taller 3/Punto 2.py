# -*- coding: utf-8 -*-
"""
@author: Andrés Otálora
"""

import numpy as np
import sympy as sp
import scipy.interpolate as sc
import matplotlib.pyplot as plt
x = np.array([0, 1, 2])
y = np.array([10,15,5])
dx = np.array([1,4,2])
interpolacion = sc.CubicHermiteSpline(x, y, dx)
a = np.linspace(0, 2, 300) 
b = interpolacion(a)
plt.plot(a, b)
plt.title("Interpolacion")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

dpoly = interpolacion.derivative()
d= dpoly(a)
plt.plot(a, d)
plt.title("Derivada polinomio interpolacion")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
print("el valor de la derivada en 0 es: ",dpoly(0))


