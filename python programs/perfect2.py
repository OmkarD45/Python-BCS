m=int(input("enter the limit"))
n=1
while(n<=m):
	i=1
	sum=0
	while(i<n):
		if(n%i==0):
			sum=sum+i
		i=i+1
	if(sum==n):
		print(n,"the no is perfect")
	n=n+1