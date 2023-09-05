def union(s1,s2):
	s3=s1|s2
	print("union of two set is",s3)
def intersection(s1,s2):
	s3=s1&s2
	print("intersetion of two set is",s3)
def difference(s1,s2):
	s3=s1-s2
	print("differnce of two set is (s1-s2)",s3)
	s4=s2-s1	
	print("differnce of two set is (s2-s1)",s4)
def length(s1,s2):
	print("length of s1 is",len(s1))
	print("length of s2 is",len(s2))
def copyset(s1,s2):
	s3=s1.copy()
	print("after copy s3 will be",s3)
def dis(s1,s2):
	if(s1.isdisjoint(s2)):
		print("s1 is disjoint to s2")
	else:
		print("some elements are same")
n=int(input("enter te set1 limit"))
s1=set()
for i in range(1,n+1):
	x=int(input("enter nos"))
	s1.add(x)
m=int(input("enter the set2 limit"))
s2=set()
for i in range(1,m+1):
	x=int(input("enter the nos"))
	s2.add(x)
union(s1,s2)
intersection(s1,s2)
difference(s1,s2)
length(s1,s2)
copyset(s1,s2)
dis(s1,s2)