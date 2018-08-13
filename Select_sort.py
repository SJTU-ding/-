#简单选择排序，交换移动数据次数少，最好的时候交换0次，最差的时候，交换次数为n-1次，比较次数为(n-1)n/2次
def SelectSort(Sqlist):
	for i in range(len(Sqlist)):
		min=i
		for j in range(i+1,len(Sqlist)):
			if Sqlist[j]<min:
				min=j
		if i!=min:
			Sqlist[i],Sqlist[min]=Sqlist[min],Sqlist[i]
SelectSort([5,4,3,2,1])
