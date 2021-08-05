import math

# n dato
# e error permitido
# x valor inicial
# y respuesta calculada con error E


def raizTarea(dato, error, inicial):
    if dato <= 0:
        return 0
    else:
        aux = 0
        y: float
        y = 0.5 * (inicial + (dato / inicial))
        while abs(inicial - y) > error:
            inicial = y
            y = 0.5 * (inicial + (dato / inicial))
            print("iteracion    "+str(aux)+": "+str(y))
            aux += 1
        return y

# 10-8 0.00000001
# 10-16 0.0000000000000001


raiz: int
ini: float

raiz = int(input('Ingrese el valor a sacar raiz: '))
ini = float(input('Ingrese el valor inicial con el que desea probar: '))

print("raiz babilonia con error -8: ")
r8 = raizTarea(raiz, 10**-8, ini)
print("Final de 10^-8: "+str(r8) + "\n\n")

print("raiz babilonia con error -16: ")
r16 = raizTarea(raiz, 10**-16, ini)
print("Final   10^-16: "+str(r16))

if(r8 == r16):
    print("\n--Ambas son iguales--")
    if(r8 == math.sqrt(raiz)):
        print("\n--La raiz de babilonia es igual con la funcion math--")
