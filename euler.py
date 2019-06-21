import numpy as np


def funcion(x,y):
    ec=x+y
    return ec

h=float(input("Tamanho do passo: "))
s=float(input("Até qual valor? "))
n=int((s/h)+1)

x=np.zeros(n)
y=np.zeros(n)


for i in np.arange(1,n):
    y[i]=y[i-1]+(funcion(x[i-1],y[i-1]))*h
    x[i]=x[i-1]+h
print(y[i])

