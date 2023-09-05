def sum(n):
	sum=5
	i=1
	ssum=0
	k=0
	for i in range(1,n+1):
		ssum=sum+ssum
		sum=sum+k
		k=i*5
		i=i+1
	print("the sum of pattern =",ssum)
n=int(input("enter the limit"))	
sum(n)