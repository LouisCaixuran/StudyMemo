import random
p=0
for i in range(10000):
	a=random.uniform(-1,1)
	b=random.uniform(-1,1)
	if (a**2+b**2)<=1:
		p+=1

pi=(p/10000.0)*4.0
print pi

