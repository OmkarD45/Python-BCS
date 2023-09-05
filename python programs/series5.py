n=int(input("enter the limit"))
sum=0 
m=1
for i in range (1,n+1):
	m=m**i
	f=1
	j=1
	while(j<=i):
		f=f*j
		j=j+1
	sum=sum+(m/f)
	m=m+1
print("sum of series is",sum)