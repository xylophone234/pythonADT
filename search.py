# search
def linearSerch(seq,value):
	n=len(seq)
	for i in range(n):
		if seq[i]==value:return i
	return None

def binarySearch(seq,value):
	low=0
	high=len(seq)-1
	while low<=high:
		mid=low+int((high-low)/2)
		if seq[mid]==value:
			return mid
		elif value<seq[mid]:
			high=mid-1
		else:
			low=mid+1
	return None