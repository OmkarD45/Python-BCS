class employee:
	def accept(self):
		self.id=int(input("enter the id\t"))
		self.name=input("enter the name\t")
		self.salary=float(input("enter the salary"))
	def display(self):
		print("ID=",self.id)
		print("NAME=",self.name)
		print("SALARY=",self.salary)

E=employee()
E.accept
E.display	