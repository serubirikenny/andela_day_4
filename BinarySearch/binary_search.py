class BinarySearch(list):
	def __init__(self, a,b):
		arr=[x for x in range(b,(a*b)+1,b)]
		self.length=len(arr)
		super(BinarySearch, self).__init__(arr)


	def search(self,term):
		pass