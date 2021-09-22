import numpy as np

#Punto 6

#Metodo de Jacobi
def MetJacobi (A, b, x0, t, it):
    MDiag = np.diag(np.diag(A))
    LU = A-MDiag
    x = x0
    for i in range (it):
        MDiagI = np.linalg.inv(MDiag)
        xAux = x
        x = (MDiagI @ (-LU) @ x) + MDiagI @ b
        print('Iteracion: ', i, ' Solucion: ',x)
        if(np.linalg.norm(x-xAux)<t):
          return x
    return x

#Metodo de Gauss Seidel
def MetGaussSeidel (A, b, x0, t, it):
    iteracion = 0
    x = x0
    while iteracion<it:
      for i in range (len(A)):
        cont = 0
        for j in range (len(A)):
          if j != i:
            cont = cont + A[i][j]*x[j]
        xAux = (b[i] - cont)/A[i][i]
        x[i] = xAux
      iteracion=iteracion+1
      print('Iteracion: ', iteracion, ' Solucion: ',x)
    return x

#Definicion de matrices


A = np.array([[2, 0, -1], [0, 2, -1], [-1, 1, 3]])
b = np.array([1, 2, 1])
x0 = np.array([1, 2, 3])

print('Solucion por Jacobi:')

x= x = MetJacobi(A,b,x0,1**-10,10)

print('Solucion por Gauss Seidel:')

x = MetGaussSeidel(A,b,x0,1**-10,10)