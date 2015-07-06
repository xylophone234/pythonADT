# Array
import ctypes
class Array():
	# creates an array with size elements.
	def __init__(self,size):
		assert size >0 ,'Array size must be > )'
		self._size=size
		# create the array structure using hte ctyepes module.
		PyArrayType=ctypes.py_object*size
		self._elements=PyArrayType()
		# Inint each element
		self.clear(None)

	# Retruns the size of the array.
	def __len__(self):
		return self._size

	# Gets the contents of the index element.
	def __getitem__(self,index):
		assert index >=0 and index <len(self),'Array subscript out of range'
		return self._elements[index]

	# Set the contests of the index element.
	def __setitem__(self,index,value):
		assert index>=0 and index <len(self),'array subscript out of range'
		self._elements[index]=value

	# Clears the array by setting each element to the given value.
	def clear(self,value):
		for i in range(len(self)):
			self._elements[i]=value

	# Return the array's iterator for traversing the elements.
	def __iter__(self):
		return _ArrayIterator(self._elements)

# An interator for the Array ADT.
class _ArrayIterator():
	def __init__(self,theArray):
		self._arrayRef=theArray
		self._currentIndex=0

	def __iter__(self):
		return self

	def __next__(self):
		if self._currentIndex<len(self._arrayRef):
			entry=self._arrayRef[self._currentIndex]
			self._currentIndex+=1
			return entry
		else:
			raise StopIteration

class Array2D():

	def __init__(self,numRows,numCols):

		self._theRows=Array(numRows)

		for i in range(numRows):
			self._theRows[i]=Array(numCols)

	def numRows(self):
		return len(self._theRows)

	def numCols(self):
		return len(self._theRows[0])

	def clear(self,value):
		for row in range(self.numRows()):
			row.clear(value)

	def __getitem__(self,indexTuple):
		assert len(indexTuple)==2,'Invalid number of array subscripts.'
		row=indexTuple[0]
		col=indexTuple[1]
		assert row>=0 and row<self.numRows()\
			and col>=0 and col<slef.numCols(),\
				'Array subscript out of range.'
		the1dArray=self._theRows[row]
		return the1dArray[col]

	def __setitem__(self,indexTuple,value):
		assert len(indexTuple==2),'Invalid number of array subscripts.'
		row=indexTuple[0]
		col=indexTuple[1]
		assert row>=0 and row<self.numRows()\
			and col>=0 and col<slef.numCols(),\
				'Array subscript out of range.'
		the1dArray=self._theRows[row]
		the1dArray[col]=value



