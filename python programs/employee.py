class employee:
	id=0
	name=""
	salary=0.0
	def accept(self):
		self.id=int(input("enter the id:\t"))
		self.name=input("enter the name:\t")
		self.salary=float(input("enter the salary:\t"))
	def display(self):
		print("ID=",self.id)
		print("NAME=",self.name)
		print("SALARY=",self.salary)

E=employee()
E.accept()
E.display()