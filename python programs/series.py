n=int(input("enter the limit"))
i=3;f1=0;f2=3;f3=0;
print(f1," ",f2," ",end='')
while(i<=n):
	f3=f2+f1
	print("",f3," ",end='')
	f1=f2
	f2=f3

	i=i+1