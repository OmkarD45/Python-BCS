n=("enter the limit")
i=1
sum=0
while(i<n+1):
	j=1
	while(j<=i):
		fact=fact*j
		j=j+1
	sum=sum+fact
	i=i+1
print("sum of series is",sum)