#with argument with return

def fact(n):
	i=1
	fact=1
	while(i<=n):
		fact=fact*i
		i=i+1
	return fact
n=int(input("enter the limit"))	
sum=0
i=1
while(i<=n):
	sum=sum+fact(i)
	i=i+1
print("the sum of series is",sum)