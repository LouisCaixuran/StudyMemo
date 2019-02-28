import numpy as np
from scipy import integrate
import random


def f1(x):
	return x*x

def f2(x):
	return -x*x+1

def use_scipy_integrate():
	low=0.6
	high=0.8
	xpoint=(low+high)/2.0
	while np.abs(f1(xpoint)-f2(xpoint))>=0.001:
		xpoint=(low+high)/2.0
		if f1(xpoint)>f2(xpoint):
			high=xpoint
		elif f1(xpoint)<f2(xpoint):
			low=xpoint


	a,e=integrate.quad(f1,0,xpoint)
	b,e=integrate.quad(f2,0,xpoint)
	print(b-a)

def definite_integrate(delta=0.001):
	x=0
	answer=0
	while(f2(x)>f1(x)):
		answer += (f2(x)-f1(x))*delta
		x = x + delta

	print(answer)

def mtc(count=10000):
	num=0.0
	for i in range(count):
		x=random.uniform(0,1)
		y=random.uniform(0,1)
		if f2(x)>y and f1(x)<y:
			num=num+1
	answer=num/count
	print(answer)

mtc(100000)


