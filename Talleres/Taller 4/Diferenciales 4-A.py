# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#Crear los preparativos
f = lambda t,x,y : 0.4*x -0.018*x*y
g = lambda t,x,y : -0.8*y + 0.023*x*y




#Ecuacion de Euler
def euler(f, g, t, x, y, h, n):
    #crear los espacios en ceros 
    valor = np.zeros(shape=(n+1,3),dtype=float)
    valor[0] = [t, x, y]
    #preparar valores auxiliares para el ciclo 
    au1 = t
    au2 = x
    au3 = y
    
    #ciclo del procedimiento
    for i in range(1,n+1,1):
        #auxiliares para almacenar creacion de datos
        K1x = h * f(t, x, y)
        K1y = h * g(au1,au2,au3)        
        K2x = h * f(au1+h, au2 + K1x, au3+K1y)
        K2y = h * g(au1+h, au2 + K1x, au3+K1y)
        au2 = au2 + (1/2)*(K1x+K2x)
        au3 = au3 + (1/2)*(K1y+K2y)
        au1 = au1 + h        
        valor[i] = [au1,round(au2,1),round(au3,1)]
    return(valor)
 
valor = euler(f, g, 0, 30, 4, 1, 20)

#separar los datos obtenidos de Euler
tval=valor[:,0]
xval=valor[:,1]
yval=valor[:,2]

#agregar los años a tval
for i in range(len(tval)):
    tval[i]+=1900.0

print("Solucion numerica del sistema de ecuaciones (año, conejo, linces) ")
print(valor)


#Graficar
plt.plot(tval,xval, label='presa')
plt.plot(tval,yval, label='predador')

plt.title('Comparacion depredadores y presas')
plt.xlabel('año')
plt.ylabel('cantidad')
plt.legend()
plt.grid()
plt.show()

# gráfica conejos vs presas
plt.plot(xval,yval)

