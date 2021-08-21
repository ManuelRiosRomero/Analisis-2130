import math

def funcion_biseccion(funcion,inicio_intervalo,fin_intervalo,iteraciones, tolerancia):
    if funcion(inicio_intervalo)*funcion(fin_intervalo) >= 0:
        print("No funciona metodo de biseccion")
        return None
    aux1 = inicio_intervalo
    aux2 = fin_intervalo
    iteracionN = 1
    #for n in range(1,iteraciones+1):
    condicion = True
    while condicion:
        iteracionN = iteracionN + 1
        medio = (aux1 + aux2)/2
        if funcion(aux1)* funcion(medio) < 0:
            aux2 = medio
        elif funcion(aux2)*funcion(medio) < 0:
            aux1 = medio
        elif funcion(medio) == 0:
            print("Se encontro la solucion exacta")
            return medio
        else:
            print("No se puede usar biseccion")
            return None
        if iteracionN > iteraciones:
            print("Se alcanzo el maximo de iteraciones")
            return (aux1 + aux2)/2
        
        condicion = abs(funcion(medio)) > tolerancia
    ("Se encontro la solucion")
    return (aux1 + aux2)/2

def PuntoFijoCalcular(funcion,funcion2, referencia, tolerancia, iter):
    iteracionN = 1
    aux = 1
    condicion = True
    while condicion:
        x = funcion2(referencia)
        #print('Iteracion numero %d, el valor del punto fijo = %0.6f y  la funcion en este punto = %0.6f' % (iteracionN, x, funcion(x)))
        referencia = x

        iteracionN = iteracionN + 1
        
        if iteracionN > iter:
            aux=0
            print("\nSe alcanzo el maximo de iteraciones")
            break
        
        condicion = abs(funcion(x)) > tolerancia
        
    if aux==1:
        print('\nLa raiz para esta funcion es: %0.8f y la funcion en este punto = %0.8f' % (x, funcion(x)))
    else:
      print('El valor del punto fijo = %0.8f y  la funcion en este punto = %0.8f' % (x, funcion(x)))
#Lista de rangos para biseccion
# para g -1 y 1, para h -1 y 1,  


#Ejecucion
#valor tolerancia
TOL= 10**(-7)
#Numero de iteraciones
n=100
#punto de referencia para punto fijo
r=-1
#Inicio intervalo biseccion
inicio = -0.1
#fin intervalo biseccion
fin=3
#Funcion de aproximacion para punto fijo
#fpuntofijo= lambda x: -1/(math.cos(x**2))
gpuntofijo=lambda x: math.cos(x)
hpuntofijo= lambda x: math.exp(x)-1
ipuntofijo = lambda x: 8/(27*(x**2-2*x+4/3))
kpuntofijo = lambda x: 5/(x**2 - 2)

#Funciones
#f = lambda x: x*(math.cos(x**2)) + 1
g = lambda x: (math.cos(x))*(math.cos(x)) - x*x
h = lambda x: math.exp(x) - x -1
i = lambda x: x*x*x - 2*x*x + (4/3)*x - (8/27)
k = lambda x: x*x*x - 2*x - 5

#Se llama la funcion con los parametros(funcion, inicio del intervalo, fin del intervalo, numero de iteraciones, tolerancia)
respuesta = funcion_biseccion(k,inicio,fin,n,TOL)
try:
  print('el resultado para el metodo de biseccion es: %0.8f'% respuesta)
except OverflowError:
    None
except TypeError:
    None
#para saber el valor de la funcion en biseccion, cambiar la g por la funcion correspondiente.
try:
  print('el valor de la funcion en ese punto es: %0.8f'% k(respuesta))
except OverflowError:
  None
except TypeError:
  None
#Se llama la funcion para el calculo por punto fijo de la forma (funcion, funcion aproximada, punto de referencia, tolerancia, numero de iteraciones)
respuesta = PuntoFijoCalcular(k,kpuntofijo,r,TOL,n)
