import numpy as np

x=np.array([[1,0.13537,0.56715],
			[1,0.93574,0.17782],
			[1,0.49753,0.38973],
			[1,0.44998,0.77891],
			[1,0.24773,0.46366]])
y=np.array([[0.42697],
			[0.42914],
			[0.42770],
			[0.50078],
			[0.41750]])
w=np.zeros((len(x.T),len(y.T)))

def gradient(x,y,w):
	return (1.0/len(y))*(np.dot(x.T,np.dot(x,w)-y))

def train(x,y,w,optimizer=0.5):
	n=np.dot(x,w)-y
	while not np.all(np.absolute(n)<=1e-5):
		w=w-optimizer*gradient(x,y,w)
		n=np.dot(x,w)-y
	return w

w=train(x,y,w)
print w
