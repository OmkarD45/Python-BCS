n=int(input("enter the no"))
revno=0
while(n>0):
	r=n%10
	revno=(revno*10)+r
	n=n//10
print("rev no is",revno)







#if we enter 234 then o/p will treated as follows
#enter the no234
#r= 4
#revno= 4
#r= 3
#revno= 43
#r= 2
#revno= 432
#rev no is 432