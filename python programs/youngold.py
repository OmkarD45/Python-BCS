a=int(input("enter the age of first person "))
b=int(input("enter the age of second person "))
c=int(input("enter the age of third person "))
if(a>b and a>c):
	if(b>c):
		print("third person is youngest")
	else:
		print("second person is youngest")
	print("first person is oldest") 
elif(b>a and b>c):
	if(a>c):
		print("third person is youngest")
	else:
		print("first person is youngest")
	print("second person is oldest") 
elif(c>a and c>b):
	if(a>b):
		print("second person is youngest")
	else:
		print("first person is youngest")
	print("third person is oldest") 