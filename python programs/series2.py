n=int(input("enter the limit"))
i=1
sum=0
while(i<=n):
	j=1
	fact=1
	while(j<=i):
		fact=fact*j
		j=j+1
	sum=sum+fact
	i=i+2
print("sum of series is",sum)