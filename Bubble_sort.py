#冒泡法1：从上到下，j从i+1到最后一个数，依次和i的当前位置的数进行比较和交换
# def Bubble_sort(Sqlist):
# 	for i in range(len(Sqlist)-1):
# 		for j in range(i+1,len(Sqlist)):
# 			if Sqlist[i]>Sqlist[j]:
# 				Sqlist[i],Sqlist[j]=Sqlist[j],Sqlist[i]
# 	print(Sqlist)
# Bubble_sort([5,4,3,2,1])

#冒泡法2：j从下到i，每次比较相邻元素，交换
# def Bubble_Sort(Sqlist):
# 	for i in range(len(Sqlist)):
# 		for j in range(len(Sqlist)-1,i,-1): #从最后一个元素向前遍历，到i结束，i为第i项
# 			if Sqlist[j]<Sqlist[j-1]:
# 				Sqlist[j],Sqlist[j-1]=Sqlist[j-1],Sqlist[j]
# 	print(Sqlist)
# Bubble_Sort([5,4,3,2,1])

#冒泡法3：增加哨兵flag，flag初始为false，若发生交换则变为true,若i等于某个数时已有序，不再往下比较
def Bubble_Sort(Sqlist):
	flag=True
	for i in range(len(Sqlist)):
		if (flag):
			flag = False
			for j in range(len(Sqlist)-1,i,-1): #从最后一个元素向前遍历，到i结束，i为第i项
				if Sqlist[j]<Sqlist[j-1]:
					Sqlist[j],Sqlist[j-1]=Sqlist[j-1],Sqlist[j]
					flag=True
	print(Sqlist)
Bubble_Sort([5,4,3,2,1])
