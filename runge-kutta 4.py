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
    x[i]=x[i-1]+h
    K1=funcion(x[i-1],y[i-1])
    K2=funcion(x[i-1]+(h/2),y[i-1]+((h/2)*K1))
    K3=funcion(x[i-1]+(h/2),y[i-1]+((h/2)*K2))
    K4=funcion(x[i-1]+h,y[i-1]+ (h*K3))
    y[i]=y[i-1]+(h/6)*(K1+ (2*K2)+ (2*K3) + K4)
print(y[i])



                       

