""" program of list
sort = it sort the list by ascending and descending order
insert = these function is used to insert element in a list at particular pos
remove = to remove or delete element from list with their value
append = add the element at the end of list
extend = these method is used to add multiple element extend the list by another list
"""

class listpro:
	def listfun(self):
		l1=[3,4,1,6,5,2]
		print("original list is:\t\t",l1)
		l1.sort()
		print("sorted list is:\t\t\t",l1)
		l1.insert(3,8)
		print("after insertion list is:\t",l1)
		l1.remove(8)
		print("after remove list is:\t\t",l1)
		l1.append(80)
		print("after append list is:\t\t",l1)
		l1.extend([10,20,30,40])
		print("after extend list is:\t\t",l1)		
a=listpro()
a.listfun()