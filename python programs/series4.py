n=int(input("enter the limit"))
sum=0 
for i in range (1,n+1):
	i=i**i
	sum=sum+i
print("sum of series is",sum)