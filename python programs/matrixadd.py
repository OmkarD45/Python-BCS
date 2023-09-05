row=int(input("enter the no of row"))
col=int(input("enter the no of columns"))
m1=[]
m2=[]
print("enter the matrix first")
for i in range(0,row):
	a=[]
	for j in range(0,col):
		x=int(input("enter the nos."))
		a.append(x)
	m1.append(a)
print("enter the second matrix")
for i in range(0,row):
	a=[]
	for j in range(0,col):
		x=int(input("enter the nos."))
		a.append(x)
	m2.append(a)
m3=[]
for i in range(0,row):
	x=[]
	for j in range(0,col):
		x.append(0)
	m3.append(x)
for i in range(0,row):
	for j in range(0,col):
		m3[i][j]=m1[i][j]+m2[i][j]
for i in range(0,row):
	for j in range(0,col):
		print(m3[i][j],end=" ")
	print("")