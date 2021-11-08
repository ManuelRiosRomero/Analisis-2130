import numpy as np
import scipy.interpolate as itp
import matplotlib.pyplot as pt

# -----Datos base de trabajo-----
a1 = np.array([4410000, 4830000, 5250000, 5670000])
a2 = np.array([1165978, 1329190, 1501474, 1682830])
an1 = np.array([4830000, 5250000, 5670000])
an2 = np.array([1329190, 1501474, 1682830])

A = itp.interp1d(a1, a2)
B = itp.lagrange(an1, an2)
C = itp.lagrange(a1, a2)

#procedimiento de interpolacion
print("Resultados obtenidos por interpolacion")
print("Lineal = {:.3f}".format(A(5000000)))
print("Grado 1 = {:.3f}".format(B(5000000)))
print("Grado 2 = {:.3f}".format(C(5000000)))

#Grafica de comprobacion 
pt.plot(a1,a2,color='red')
pt.plot(an1,an2,color='blue',linestyle='-')
pt.plot(5000000,A(5000000),marker='X',color='black')
pt.xlabel("Base")
pt.ylabel("Cuota")
pt.show()
