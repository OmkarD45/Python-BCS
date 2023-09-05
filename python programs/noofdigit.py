n=int(input("enter the no"))
count=0
while(n>0):
	r=n%10
	count=count+1
	n=n/10
print("total no of digit in a no is",count)
