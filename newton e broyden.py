# -*- coding: utf-8 -*-

import math
from sympy import*
import numpy as np
from numpy.linalg import inv as inversa
from numpy.linalg import norm as norma


def metodo_newton_e_broyden(sistema,variaveis,Xo,Bo=[]):	
	#Se Xo=[2,3] e variáveis=[a,b], aqui estarei fazendo algo do tipo: a=2 e b=3
	parametros={}
	for i in range(len(variaveis)):
		parametros[variaveis[i]]=Xo[i]
	
	#Se Xo=[2,3], aqui estarei fazendo f(2,3)
	f_xo=[f.evalf(subs=parametros) for f in sistema]
	
	#Se o Bo=Jacobiano(Xo) não tiver sido dado, então se trata do método de Newton e não o de Broyden, daí estou calculando-o abaixo
	if Bo==[]:
		j_xo=[]
		for f in sistema:
			j_xo.append([])
			for i in variaveis:
				j_xo[-1].append(diff(f,i).evalf(subs=parametros))
	else:
		j_xo=Bo
	
	f_xo=np.array(f_xo,dtype='float')
	j_xo=np.array(j_xo,dtype='float')
	Xo=np.array(Xo,dtype='float')
	
	#obs: M.dot(N)=MxN
	delta_x=-1*inversa(j_xo).dot(f_xo)
	X=Xo+delta_x
	
	tolerancia=norma(delta_x)/norma(X)

	if tolerancia>0.0001:
		if Bo==[]: #método de Newton
			return metodo_newton_e_broyden(sistema,variaveis,X)
		else: #método de Broyden
			novos_parametros={}
			for i in range(len(variaveis)):
				novos_parametros[variaveis[i]]=X[i]
			
			f_x=[f.evalf(subs=novos_parametros) for f in sistema]
			f_x=np.array(f_x,dtype='float')
			B=j_xo-(f_x-f_xo+j_xo.dot(delta_x))/norma(delta_x)**2
			return metodo_newton_e_broyden(sistema,variaveis,X,B)
	else:
		X=[round(i,10) for i in X] #arredondarei o X com precisão até a sua décima casa decimal para que o resultado seja mais legível
		return X

#exemplo do método de Newton
a,b=symbols('a b',real=True)
sistema=[a+2*b-2,a**2+4*b**2-4]
variaveis=[a,b]
Xo=[2,3]
print(u'Resultado do exemplo do Método de Newton:\n%s'%metodo_newton_e_broyden(sistema,variaveis,Xo))

#exemplo do método de Broyden
Bo=[[1,2],[4,24]]
print(u'\nResultado do exemplo do Método de Broyden:\n%s'%metodo_newton_e_broyden(sistema,variaveis,Xo,Bo))
