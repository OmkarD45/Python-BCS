class employee:
	def display(self,id,name,salary):
		print("ID=",id)
		print("NAME=",name)
		print("SALARY=",salary)

E=employee()
id=int(input("enter the id:\t"))
name=input("enter the name:\t")
salary=float(input("enter the salary:\t"))
E.display(id,name,salary)