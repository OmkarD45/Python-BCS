class teacher:
	def get(self):
		self.tid=int(input("enter the teacher id:\t"))
		self.name=input("enter the teacher name:\t")
		self.ttype=input("enter the teacher type:\t")
		self.exp=int(input("enter the teacher type"))
	def check(self):
		if(self.ttype=='temp' and self.exp==0):
			designation='CHB'
		elif(self.ttype=='temp' and self.exp>0 and self.exp<=3):
			designation='LECTURER'
		elif(self.ttype=='permanent' and self.exp>3 and self.exp<8):
			designation='ASST.PROF'
		else:
			designation='ASSO.PROF'
	def display(self):
		print(self.tid,"\t",self.name,"\t",self.ttype,"\t",self.exp,"\t",self.designation)
n=int(input("enter the no of teachers"))
for  i in range(1,n+1):
	e1=[]
for  i in range(1,n+1):
	e1.append(teacher())
	e1[i].get()
print("ID\t\tNAME\t\tTTYPE\t\tEXPERIENCE\t\tDESIGNATION")
for i in range(0,n):
	e1[i].check()
	e1[i].display()