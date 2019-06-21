# -*- coding: utf-8 -*-

import math
from sympy import*
import numpy as np
from numpy.linalg import inv as inversa
from numpy.linalg import norm as norma

			
def ajuste_funcao_nao_linear(x_,y_,X,Y):
	u'''Explicação detalhada:
	Suponha-se que eu tenha um f(x)=algo qualquer. Por exemplo:
	y=f(x)=e*((x^a)/b)
	
	Agora, transformarei esta função em y'=a'x'+b', com:
	a'=f1(a)
	b'=f2(b)
	x'=f3(x)
	y'=f4(y)
	
	Agora, chuto dou valores quaisquer para x e y. Ex:
	(x,y)=[(x1,y1),(x2,y2),(x3,y3)]
	Assim, x' e y' terão valores:
	(x',y')=[(x'1,y'1),(x'2,y'2),(x'3,y'3)]
	
	Então faço:
	P=[[1,x'1],[1,x'2],[1,x'3]]
	B=[b',a']
	Y'=[y'1,y'2,y'3]
	P.B=Y'
		Logo:
	P^t.P.B=P^t.Y'
	daí:
	B=((P^t.P)^-1).P^t.Y'
	Daí acho a' e b' e, consequentemente, a e b
	
	Logo, o que preciso para utiliar esta função é:
	x_ que é a função de conversão de x em x'
	y_ que é a função de conversão de y em y'
	X=[x1,x2,...]
	Y=[y1,y2,...]
	
	Daí com isso consigo achar:
	X_=X'=[x'1,x'2,...]
	Y_=Y'=[y'1,y'2,...]
	
	e então será retornado a' e b'.
	'''
	x,y=symbols('x y',real=True)
	
	#explicação do que farei abaixo:
	X_=[float(x_.evalf(subs={x:i})) for i in X]
	Y_=[float(y_.evalf(subs={y:i})) for i in Y]
	
	P=np.array([[1,x] for x in X_])
	Pt=np.matrix.transpose(P)
	B=inversa(Pt.dot(P)).dot(Pt).dot(Y_)
	return B

#exemplo de ajuste de função não linear
#y=f(x)=e*((x^a)/b) então ln(ln(y))=a.ln(x)-ln(b)
#y'=a'x'+b'
#y_=y'=ln(ln(y))
#x_=ln(x)
#a'=a
#b'=-ln(b)
x,y=symbols('x y',real=True)
x_=ln(x)
y_=ln(ln(y))
X=[1,2,3]
Y=[1.995,1.410,1.260]
b_,a_=ajuste_funcao_nao_linear(x_,y_,X,Y)
a=a_
b=math.exp(-b_)
print(u'\nResultado do exemplo do Ajuste de funções não linerares:\n[a,b]=%s'%[a,b])
