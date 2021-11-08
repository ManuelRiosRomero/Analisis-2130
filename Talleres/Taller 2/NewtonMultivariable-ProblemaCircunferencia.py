#ANALISIS NUMERICO 2021-2
#TALLER 2 
#METODO DE NEWTON MULTIVARIABLE
from sympy import *
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#DEFINICION DEL SISTEMA DE 3 ECUACIONES
def matriz():
  f1= x**2
  f2=y**2
  f3=z**2
  return Matrix([[f1],[f2],[f3]])
#JACOBIANO DEL SISTEMA DE 3 ECUACIONES
def Jacobiana():
  f1= x**2
  f2=y**2
  f3=z**2
  J= Matrix([[Derivative(f1,x).doit(),Derivative(f1,y).doit(),Derivative(f1,z).doit()],[Derivative(f2,x).doit(),Derivative(f2,y).doit(),Derivative(f2,z).doit()],[Derivative(f3,x).doit(),Derivative(f3,y).doit(),Derivative(f3,z).doit()]])
  Jinv= J.inv()
  return [J, Jinv]

#DEFINICION DEL SISTEMA DE 2 ECUACIONES
def matrizP():
  f1= x**2+ y**2 -1
  f2= y - x
  return Matrix([[f1],[f2]])
#DEFINICIO DEL JACOBIANO DE 2 ECUACIONES
def JacobianaP():
  f1= x**2+ y**2 -1
  f2= y - x
  J= Matrix([[Derivative(f1,x).doit(),Derivative(f1,y).doit()],[Derivative(f2,x).doit(),Derivative(f2,y).doit()]])
  Jinv= J.inv()
  return [J, Jinv]

#DATOS
#Para 3 variables 3 ecuaciones
aprox=[2,3,4]
a, b, c = aprox
#Para 2 variables 2 ecuaciones
aprox2=[1,1]
d,f= aprox2
#Inicio de iteraciones
k=0
#Tolerancia
TOL=10 **-6
#Maximo de iteraciones
iter=25

#Se crean las matrices de funciones
#Para 3 ecuaciones
M=matriz()
J, Jinv = Jacobiana()
#Para 2 ecuaciones
M2=matrizP()
J2, Jinv2 = JacobianaP()
#Imprimir matrices
print("Matriz ecuaciones")
pprint(M2)
print("\n")
print("Matriz Jacobiana")
pprint(J2)
print("\n")
print("Matriz Jacobiana inversa")
pprint(Jinv2)
print("\n")

#CALCULO DEL METODO
print("Resultado Metodo de Newton Multivariable")

'''
#PARA 3 VARIABLES
while k<iter:
  #Sustituir valores en las matrices
  MSub= M.subs({x:a,y:b,z:c})
  JSub= J.subs({x:a,y:b,z:c})
  JinvSub = Jinv.subs({x:a,y:b,z:c})

  #Verificar substitucion

  #Comentar si se usa
  pprint(MSub)
  print("\n")
  pprint(JSub)
  print("\n")
  pprint(JinvSub)
  print("\n")

  #Calculos
  N=-JinvSub*MSub
  #pprint(N)
  X=Matrix([a, b, c]) + N
  #pprint(X)
  a2 =float(X[0,0])
  b2=float(X[1,0])
  c2=float(X[2,0])
  a,b,c=a2,b2,c2
  error=float(sqrt(N[0,0]**2+ N[1,0]**2+ N[2,0]**2))
  k+=1
  if(error < TOL):
    print("\nSe soluciono el metodo")
    print("{0:1d} \t {1:1.8f} \t {2:1.8f} \t {3:1.8f} \t {4:1.12f}".format(k,a2,b2,c2,error))
    break;
  if(k==iter):
    print("\n Se alcanzo el numero maximo de iteraciones")
  print("{0:1d} \t {1:1.8f} \t {2:1.8f} \t {3:1.8f} \t {4:1.12f}".format(k,a2,b2,c2,error))
'''
#PROBLEMA CIRCUNFERENCIA 
#Para 2 VARIABLES
while k<iter:
  #Sustituir valores en las matrices
  MSub2 = M2.subs({x:d,y:f})
  JSub2 = J2.subs({x:d,y:f})
  JinvSub2 = Jinv2.subs({x:d,y:f})
  #Verificar substitucion
  '''
  pprint(MSub)
  print("\n")
  pprint(JSub)
  print("\n")
  pprint(JinvSub)
  print("\n")
  '''
  #Calculos
  N=-JinvSub2*MSub2
  #pprint(N)
  X=Matrix([d, f]) + N
  #pprint(X)
  d2 =float(X[0,0])
  f2=float(X[1,0])
  d,f=d2,f2
  error2=float(sqrt(N[0,0]**2+ N[1,0]**2))
  k+=1
  if(error2 < TOL):
    print("\nSe soluciono el metodo")
    print("{0:1d} \t {1:1.8f} \t {2:1.8f} \t {3:1.12f}".format(k,d2,f2,error2))
    break;
  if(k==iter):
    print("\n Se alcanzo el numero maximo de iteraciones")
  print("{0:1d} \t {1:1.8f} \t {2:1.8f} \t {3:1.12f}".format(k,d2,f2,error2))
print("FIN")




