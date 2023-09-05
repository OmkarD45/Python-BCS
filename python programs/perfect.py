n=int(input("enter the no"))
i=1
sum=0
while(i<n):
	if(n%i==0):
		sum=sum+i
	i=i+1
if(sum==n):
	print("the given no is perfect")
else:
	print("the given no is not perfect")