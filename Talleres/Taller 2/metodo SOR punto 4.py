import math
import numpy as np

def relajacion(A,b,x,w,tol):
  n=len(x)
  for j in range(n):
      S=0
      for i in range(n):
        S=S+A[i][j]*x[i]
      x[j]=x[i]+w*(b[i]-S)/A[j][j]
  return x

A=np.ones((81,81))
B=np.ones(81)
x=np.ones(81)
tolerancia=10**-5


for j in range(1,81):
  B[j]=math.pi
  for i in range(1,81):
    if(j==i and i>=1):A[i][j]=2
    elif(j==i+2 and i>=1 and i<=78):A[i][j]=0.5
    elif(j==i-2 and 1>=3):A[i][j]=0.5
    elif(j==i+4 and i>=1 and i<=76):A[i][j]=0.25
    elif(j==i-4 and i>=5 ):A[i][j]=0.25
    else :A[i][j]=0
 
x=relajacion(A,B,x,0.5,tolerancia); 
print(x)