n=int(input("enter the limit"))
sum=0
esum=0
osum=0
for i in range (2,n+1):
	j=1
	f=1
	while(j<=i):
		f=f*j
		j=j+1
	if(i%2==0):
		esum=esum+f
	else:
		osum=osum+f
sum=1+esum-osum
print("sum of series is",sum)