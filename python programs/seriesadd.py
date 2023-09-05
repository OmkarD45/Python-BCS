n=int(input("enter the series limit"))
r=2
i=1
x=0
sum=0
while(i<=n):
	x=x*10+2
	sum=sum+x
	i=i+1
print("the sum of give series is",sum)