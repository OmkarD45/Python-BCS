def series(n):
	f1=0
	f2=5
	f3=0
	i=1
	t=1
	s=0
	while(i<=n):
		f3=f2+(i*5)
		s=s+f3
		f2=f3
		i=i+1
	return s
def ser(n):
	i=1
	t=1
	while(i<=n):
		t=(i*5)+t
	return t
n=int(input("enter the limit"))
i=1
q=0
while(i<=n):
	q=q+(series(n)-ser(n))
print("addition is ",q)
