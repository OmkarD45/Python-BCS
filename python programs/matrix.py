col=int(input("enter the no of columns"))
row=int(input("enter the no of rows"))
m=[]
for i in range(0,row):
	a=[]
	for j in range(0,col):
		x=int(input("enter the nos"))
		a.append(x)
	m.append(a)
print("original matrix: ")
for i in range(0,row):
	for j in range(0,col):
		print(m[i][j],end=" ")
	print("")
#transpose of matrix
print("transpose of matrix:  ")
for i in range(0,row):
	for j in range(0,col):
		print(m[j][i],end=" ")
	print("")

#prime nos in matrix:
for i in range(0,row):
	for j in range(0,col):
		flag=0
		for k in range(2,m[i][j]):
			if(m[i][j]%k==0):
				flag=1
				break
		if(flag==1):
			print(m[i][j]," is not prime")
		else:
			print(m[i][j]," is prime")

#upper triangular matrix:
for i in range(0,row):
	for j in range(0,col):
		if(i>j):
			 m[i][j]=0
print("upper triangular matrix: ")
for i in range(0,row):
	for j in range(0,col):
		print(m[i][j],end=" ")
	print("")

#lower triangular matrix:
for i in range(0,row):
	for j in range(0,col):
		if(i<j):
			 m[i][j]=0
print("lower triangular of upper triangular matrix: ")
for i in range(0,row):
	for j in range(0,col):
		print(m[i][j],end=" ")
	print("")



























