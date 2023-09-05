n=int(input("enter the limit"))
f1=0
f2=5
f3=0
i=1
sum=5
print(f1," ",end='')
print(f2," ",end='')
while(i<n-1):
	f3=f2+(i*5)
	print(f3," ",end='')
	sum=sum+f3
	f2=f3
	i=i+1
print("\n sum of series is",sum)