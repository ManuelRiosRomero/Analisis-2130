import math
import numpy as np

#En esta sección se averigua a que equivale k1 , k2 y k3 a traves
#de una solución de ecuaciones lineales

a=np.array ([[10,100,4.481],[15,225,9.487],[20,400,20.085]])
b=np.array([25,130,650])
x=np.linalg.solve(a,b)
print(x)

#A partir de aqui se utilizan los resultados obtenidos 
#Para encontrar solución al objetivo a traves de iteraciones
#Se empieza con un valor de 23 para las iteraciines por lo que el 
#Programa calcula a partir de 1300 aproximadamente
e = math.e
i = 0
y = 23.000
objetivo = 2000
while i <= objetivo:
    
    i = (-17.31476212 * y) + (-2.24249889 * (y**2) ) + (94.26411739 * (e**(0.15*(y))))
    y = y + 0.0001

print ("Para el objetivo" , objetivo)
print ("el valor de t es aproximadamente", y, "El valor obtenido con este t es igual a :", i)

