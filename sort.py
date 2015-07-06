# sort
def bubbleSort(seq):
	n=len(seq)
	for i in range(n-1):
		for j in range(n-1-i):
			if seq[j]>seq[j+1]:
				temp=seq[j+1]
				seq[j+1]=seq[j]
				seq[j]=temp

def selectionSort(seq):
	n=len(seq)			
	for i in range(n-1):
		smallIndex=i
		for j in range(i+1,n):
			if seq[j]<seq[smallIndex]:smallIndex=j
		if smallIndex!=i:
			temp=seq[i]
			seq[i]=seq[smallIndex]
			seq[smallIndex]=temp