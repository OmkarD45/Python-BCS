n=int(input("enter the limit"))
sum=0
for i in range(1,n+1):
	j=1
	m=1
	while(j<=i):
		m=m*i
		j=j+1
	sum=sum+m
print("sum of series is",sum)