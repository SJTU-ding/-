class seqList():
	def __init__(self,m,l):
		self.MAXSIZE=m #线性表最大存储容量
		self.length=l  #线性表的当前长度,在任意时刻，线性表的长度都应该小于等于数组的长度
		self.data=[None]*self.MAXSIZE
	def getElements(self,i): #取值
		if not isinstance(i, int):
			raise TypeError
		if self.length==0 or i<1 or i>self.length:
			raise IndexError
		else:
			return self.data[i]
	def ListInsert(self,i,e): #在位置(索引)i处插入元素e
		if not isinstance(i,int):
			raise TypeError
		if self.length==self.MAXSIZE:
			raise OverflowError
		if i<0 or i>self.length-1:
			raise IndexError
		if i<=self.length-1:
			for k in range(self.length-1,i-2,-1):
				self.data[k+1]=self.data[k]
			self.data[i]=e
			self.length+=1
	def ListDelete(self,i):
		if not isinstance(i,int):
			raise TypeError
		if i<0 or i>self.length-1:
			raise IndexError
		else:
			for k in range(i,self.length-1):
				self.data[k]=self.data[k+1]
			self.length-=1
B=seqList(8,5)
B.ListInsert(3,10)
B.ListDelete(3)
