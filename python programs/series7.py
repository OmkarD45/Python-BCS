n=int(input("enter the limit"))
sum=0
dsum=0
for i in range(0,n+1):
	sum=sum+i
	if(i%3==0):
		if(i==3):
			dsum=2*sum
		dsum=dsum-sum
		sum=0
print("sum of series is",dsum)