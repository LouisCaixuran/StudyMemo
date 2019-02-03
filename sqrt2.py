import datetime
def ftime(func):
	def wrapper(*arg,**kw):
		a=datetime.datetime.now()
		func(*arg,**kw)
		b=datetime.datetime.now()
		print b-a
	return wrapper
@ftime
def sqrt1(n):
	res=n/2.0
	low=0.0
	high=n
	while (high-low)>0.00000000001:
		if res*res<n:
			low=res
		elif res*res>n:
			high=res

		res=(high+low)/2
	print res
	return res

@ftime
def sqrt2(n):
	res=n/2.0
	while abs(res*res-n)>0.000001:
		res=(res*1.0+(1.0*n)/res)/2.0
	print res
	return res

@ftime
def neizhisqrt(n):
	a=n**0.5
	print a
	return a


sqrt1(2)
sqrt2(2)
neizhisqrt(2)

