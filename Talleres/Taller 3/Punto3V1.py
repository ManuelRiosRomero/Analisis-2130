#RANGO DE NOTAS
# 3O-40 40-50 50-60 60-70 70-80
#   35    48    70    40    22
import numpy as np

np_list1 = np.array([35, 48, 70 , 40 , 22])

cam = np_list1 [2]
menos = np_list1[0]+ np_list1[1]
estim = menos
estim2 = menos + (cam)
estim3 = menos + (cam-10)
estim4 = menos + (cam-20)
estim5 = menos + (cam-30)
estim6 = menos + (cam-40)
estim7 = menos + (cam-50)
estim8 = menos + (cam-60)




aprox = (estim + estim2 + estim3 + estim4 + estim5 + estim6 +estim7 + estim8)/9

aprox2 = (estim + estim2)/2

aprox3 = (aprox + aprox2)/2
#print (cam , "-", estim,"-",estim2,"-",estim3,"-",estim4,"-",estim5,"-",estim6)

print("Aproximacion 1:",int(aprox) ,"-Aproximacion 2:", int (aprox2),"-Aproximacion 3:", int(aprox3), " Minimo de alumnos", menos)
