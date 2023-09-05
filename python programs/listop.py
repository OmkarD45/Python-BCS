n=int(input("enter the total element in list:\t"))
list1=[]
for i in range(0,n):
	x=int(input("enter the actual elements:\t"))
	list1.insert(i,x)
key=int(input("enter the no for counting"))
ans=list1.count(key)
print("original list is:\t",list1)
print("total occurance of ", key ,"is:", ans)
list1.sort()
print("sorted list is:\t",list1)
list1.reverse()
print("reverse of sorted list is :\t",list1)

