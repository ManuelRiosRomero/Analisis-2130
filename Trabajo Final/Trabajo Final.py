import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go
import datetime
import pylab as pl
import sympy as sy

def f(beta,S0):
    return (0.021)

#Funcion Euler mejorado

def eulerMejorado(f, x, y, h, m):
    u = np.zeros([m,2],dtype=float)
    for i in range(m):
        yn = y + h*f(x,y)
        y = y + h*(f(x,y) + f(x+h,yn))/2
        x += h
        u[i,0] = x
        u[i,1] = y
    return u

#Definicion de datos 
N = 45000
I0 = 1
R0 = 0
S0 = N - I0 - R0
beta = 0.06
gamma =  0.021
t = np.linspace(0, 1300, 1300)
R0 = (beta * 1.5 * S0) / (gamma * N)

#Definicion de ecuaciones
def deriv(y, t, N, beta, gamma):
    S, I, R, = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I

    return dSdt, dIdt, dRdt

#Solucion

sol = eulerMejorado(f,0,1,0.1,20)
np.set_printoptions(precision=5)
sy.Matrix(sol)

# Condiciones iniciales
y0 = S0, I0, R0

ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

print("Soluciones: ", ret)

#Cantidad maxima de infectados y porcentajes de poblacion

def porcentajesPob():
    Poblacion = 45000
    infectados = 1
    recuperados = 0
    contagios = 0
    suceptibles = 45000
    dias = 365

    inicio = datetime.datetime(2020, 3, 20)
    lista_fecha = [inicio]
    lista_contagios = [contagios]
    lista_recuperados = [recuperados]
    lista_suceptibles = [suceptibles]
    total_contagios = 0
    total_recuperados = 0
    total_infectados = 0


    for i in range(dias):
        contagios = infectados * 1.5 * suceptibles / Poblacion 
        contagios_estadistica = contagios * 1.25 / 100
        suceptibles = suceptibles - contagios
        inicio = inicio + datetime.timedelta(days=1)
        recuperados_dia = infectados
        recuperados = recuperados + recuperados_dia
        infectados = infectados + contagios - recuperados_dia
        total_contagios = total_contagios + contagios
        total_infectados = total_infectados + infectados
        lista_fecha.append(inicio)
        lista_contagios.append(contagios)
        lista_recuperados.append(recuperados)
        lista_suceptibles.append(suceptibles)

        primerCondicional = (gamma / (beta * 1.5))
        segundoCondicional = S / N
     
    max = 0
    fecha = 0

    for i in range(0, len(lista_contagios)):
        if (max < lista_contagios[i]):
            max = lista_contagios[i]
            fecha = lista_fecha[i]

    print("Valor maximo: ", max)
    print("Fecha en donde se presento el valor maximo: ", fecha)
    print("Fecha de inicio: ", inicio)
    print("Periodo de evaluacion: ", dias, "dias")

    PorcenteajeR = recuperados * 100 / total_contagios
    print("Porcentaje de personas recuperadas: ", round(PorcenteajeR, 2), "%")

    PorcenteajeI = total_infectados * 100 / Poblacion
    print("Porcentaje de personas infectadas: ", round(PorcenteajeI, 2), "%")


porcentajesPob()

#Grafica

fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=S,mode='lines',name = 'Suceptible'))
fig.add_trace(go.Scatter(x=t, y=I,mode='lines',name = 'Infectado'))
fig.add_trace(go.Scatter(x=t, y=R,mode='lines',name = 'Recuperado'))

fig.update_layout(
    title = "Estimacion de propagacion",
    xaxis_title = "Dias",
    yaxis_title = "Poblacion",
  
)

pl.plot(sol[:,0],sol[:,1],'ob')

fig.show()
