class BinarySearch(list):
	def __init__(self, a,b):
		arr=[x for x in range(b,(a*b)+1,b)]
		self.length=len(arr)
		super(BinarySearch, self).__init__(arr)


	def search(self,term):
		lower=0
		count=0
		upper=self.length
		found=False
		found_data={}
		
		if term==self[0] or term==self[-1]:
			return {"count":count,"index":self.index(term)}
		else:
			while lower<upper or lower !=upper and not found:
				needle=lower+(upper-lower)//2
				value=self[needle]
								
				if term==value:
					found_data["index"]=needle
					found_data["count"]=count
					found=True
					break

				elif term>value:
					if needle==lower:
						break
					lower=needle
					count+=1
				elif term<value:
					upper=needle
					count+=1

		if not found:
			return {"count":count,"index":-1}
		return found_data