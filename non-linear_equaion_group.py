import numpy as np
from scipy.optimize import root,fsolve
import math




def func(x):
	return [3*x[0]-np.cos(x[1])*x[2]-0.5,
					x[0]**2-81*(x[1]+0.1)**2+np.sin(x[2])+1.06,
					math.e**(-1*x[0]*x[1])+20*x[2]+(10*math.pi-3)/3]




#
def newton():
	x0=[0.0,0.0,0.0]
	x=[1.0,1.0,1.0]
	eps=0.0
	count=0
	for i in range(3):
		eps+=(x[i]-x0[i])**2.0
	while eps>=0.0000001:
		x[0]=1.0/3*np.cos(x0[1])*x0[2]+1.0/6
		x[1]=1.0/9*math.sqrt(x0[0]**2+np.sin(x0[2])+1.06)-0.1
		x[2]=-1.0/20*math.e**(-1*x0[0]*x0[1])-(10*math.pi-3)/60.0
		eps=0.0
		for i in range(3):
			eps+=(x[i]-x0[i])**2.0
		x0=x
		count+=1

	return x0,count

def main():
	print newton()
	#sole_root=root(func,[0,0,0])
	#ole_fsolve=fsolve(func,[0,0,0])
	#print sole_root,sole_fsolve

if __name__ == '__main__':
	main()
