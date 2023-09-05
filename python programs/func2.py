#with argument with return

def fact(n):
	i=1
	fact=1
	while(i<=n):
		fact=fact*i
		i=i+1
	return fact
def pow(n):
	i=1
	power=1
	while(i<=n):
		power=power*n
		i=i+1
	return power
n=int(input("enter the limit"))	
sum=0
i=1
while(i<=n):
	sum=sum+(pow(i)/fact(i))
	i=i+1
print("power=",pow(i),"fact",fact(i))
print("the sum of series is",sum)