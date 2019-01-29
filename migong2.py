import copy
source=[ 
    [0,0,1,0,1],
    [1,0,1,0,1],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]]  
class Migong(object):

	def __init__(self,source):
		self.source=copy.deepcopy(source)
		self.success=0

	def move(self,x,y):
		if x==4 and y==4:
			print ("success")
			self.success=1
			return True

		if (x<=4 and x>=0 and y<=4 and y>=0)  and self.success==0:	
			if self.source[x][y]==0:
				self.source[x][y]=2
				if self.move(x+1,y):
					return True
				elif self.move(x-1,y):
					return True
				elif self.move(x,y+1):
					return True
				elif self.move(x,y-1):
					return True
				else:
					self.source[x][y]=0
	
obj=Migong(source)
obj.move(0,0)
for i in range(5):
	print obj.source[i]


print
for i in range(5):
	print source[i]




